import random
import string
import threading
from enum import Enum
from functools import partial
import socket
from collections import Counter

import json
import uuid

from cardcast import CardSet
import http_server
from websocket_server import start_websocket

HOST = socket.gethostbyname(socket.gethostname())
HTTP_PORT = 80
WEBSOCKET_PORT = 8080


class Command(Enum):
    KEEP_ALIVE = "keep_alive"
    JOIN = "join"
    CREATE_SESSION = "create_session"
    ADD_CARD_SET = "add_card_set"
    # client-side
    SET_READY = "set_ready"
    PICK_CARD = "pick_card"
    # server-side
    GAME_STATE = "game_state"
    SESSION_STATE = "session_state"


class GamePhase(Enum):
    NOT_JOINED = -1
    NOT_STARTED = 0
    PICK_YOUR_CARD = 1
    PICK_BEST_CARD = 2
    ROUND_WINNER = 3


class Client:
    def __init__(self, websocket):
        self.websocket = websocket
        self.client_id = str(uuid.uuid4())
        self.score = 0
        self.ready = False
        self.deck = []
        self.username = ""

    async def send(self, packet):
        await self.websocket.send(json.dumps(packet))

    def reset(self):
        self.score = 0
        self.ready = False


class GameSession:
    def __init__(self, gm):
        self.gm = gm
        self.players = []
        self.code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        self.sets = []
        self.phase = GamePhase.NOT_STARTED
        self.current_question = ""
        self.current_answers = {}
        self.current_best_answers = {}
        self.current_highlight = ""

    async def broadcast(self, packet):
        for player in self.players:
            await player.send(packet)

    async def close(self):
        for player in self.players:
            player.reset()
            await player.send({
                "command": Command.GAME_STATE.value,
                "game_phase": GamePhase.NOT_JOINED.value,
                "deck": [],
                "options": {}
            })

    async def update_decks(self):
        if self.phase == GamePhase.PICK_BEST_CARD:
            choose_deck = [y for x, y in self.current_answers.items()]
            for player in self.players:
                copy = choose_deck
                if len(self.players) > 2:
                    copy = choose_deck.copy()
                    copy.remove(self.current_answers[player.client_id])
                await player.send({
                    "command": Command.GAME_STATE.value,
                    "deck": copy,
                    "game_phase": self.phase.value,
                    "options": self.current_answers
                })
        else:
            for player in self.players:
                while len(player.deck) < 8:
                    player.deck.append(self.get_random_answer())
                await player.send({
                    "command": Command.GAME_STATE.value,
                    "deck": player.deck,
                    "game_phase": self.phase.value,
                    "options": self.current_answers
                })

    def get_random_answer(self):
        return random.choice(random.choice(self.sets).answers)

    def get_random_question(self):
        return random.choice(random.choice(self.sets).questions)

    async def update_session(self):
        if self.phase == GamePhase.NOT_STARTED and all([x.ready for x in self.players]) and \
                len(self.sets) is not 0 and len(self.players) > 1:
            self.phase = GamePhase.PICK_YOUR_CARD
            await self.update_decks()
            self.current_question = self.get_random_question()
        if self.phase == GamePhase.PICK_YOUR_CARD and len(self.current_answers) == len(self.players):
            self.phase = GamePhase.PICK_BEST_CARD
            await self.update_decks()
        if self.phase == GamePhase.PICK_BEST_CARD and len(self.current_best_answers) == len(self.current_answers):
            self.phase = GamePhase.ROUND_WINNER
            best = sorted(Counter([y for x, y in self.current_best_answers.items()]).items())
            print(best)
            if len(best) > 1 and best[0][1] == best[1][1]:
                self.current_highlight = ""
            else:
                winner = [y for x, y in all_players.items() if y.client_id ==
                          [x for x, y in self.current_answers.items() if y == best[0][0]][0]][0]
                self.current_answers = {winner.client_id: self.current_answers[winner.client_id]}
                self.current_highlight = winner.username
                winner.score += 1
            await self.update_decks()
        await self.gm.send({
            "command": Command.SESSION_STATE.value,
            "game_phase": self.phase.value,
            "question": self.current_question,
            "answers": self.current_answers,
            "highlight": self.current_highlight,
            "players": [{"id": x.client_id, "username": x.username, "score": x.score, "ready": x.ready} for x in
                        self.players]
        })


all_players = {}
all_sessions = {}


def get_client_by_websocket(websocket):
    for s, p in all_players.items():
        if websocket == s:
            return p
    return None


def get_session_by_client(client):
    for code, session in all_sessions.items():
        if session.gm == client:
            return session
    return None


def get_session_by_player(player):
    for code, session in all_sessions.items():
        if player in session.players:
            return session
    return None


async def handle_keep_alive(websocket, packet):
    pass


async def handle_create_session(websocket, packet):
    client = get_client_by_websocket(websocket)
    print("Create session")
    session = GameSession(client)
    all_sessions[session.code] = session
    client.is_player = False
    await client.send({
        "command": Command.CREATE_SESSION.value,
        "client_id": client.client_id,
        "code": session.code
    })


async def handle_add_card_set(websocket, packet):
    client = get_client_by_websocket(websocket)
    print("Add card set " + packet["set_id"])
    session = get_session_by_client(client)
    try:
        set = CardSet(packet["set_id"])
        session.sets.append(set)
        await client.send({
            "command": Command.ADD_CARD_SET.value,
            "success": True,
            "set_name": set.name
        })
        await session.update_session()
    except (IOError, KeyError) as e:
        print("Failed to get card set with error:")
        print(e)
        await client.send({
            "command": Command.ADD_CARD_SET.value,
            "success": False,
            "set_id": packet["set_id"]
        })


async def handle_join_session(websocket, packet):
    client = get_client_by_websocket(websocket)
    code = packet["code"].upper()
    if code in all_sessions:
        session = all_sessions[code]
        if packet["username"] in [x.username for x in session.players] or packet["username"] == "":
            await client.send({
                "command": Command.JOIN.value,
                "success": False
            })
            return
        client.username = packet["username"]
        session.players.append(client)
        await session.update_session()
        await client.send({
            "command": Command.JOIN.value,
            "success": True,
            "client_id": client.client_id
        })
    else:
        await client.send({
            "command": Command.JOIN.value,
            "success": False
        })


async def handle_pick_card(websocket, packet):
    client = get_client_by_websocket(websocket)
    session = get_session_by_player(client)
    if session.phase == GamePhase.PICK_YOUR_CARD and client.client_id not in session.current_answers \
            and packet["card_id"] in client.deck:
        session.current_answers[client.client_id] = packet["card_id"]
        client.deck.remove(packet["card_id"])
        await session.update_session()
    elif session.phase == GamePhase.PICK_BEST_CARD and client.client_id not in session.current_best_answers \
            and packet["card_id"] in [y for x, y in session.current_answers.items()]:
        session.current_best_answers[client.client_id] = packet["card_id"]
        await session.update_session()


async def handle_client_ready(websocket, packet):
    client = get_client_by_websocket(websocket)
    for code, session in all_sessions.items():
        if client in session.players:
            client.ready = packet["ready"]
            await session.update_session()


async def handle_session_state(websocket, packet):
    client = get_client_by_websocket(websocket)
    session = get_session_by_client(client)
    if session is not None and session.phase == GamePhase.ROUND_WINNER:
        session.phase = GamePhase.NOT_STARTED
        session.current_answers = {}
        session.current_best_answers = {}
        session.current_highlight = ""
        await session.update_session()


async def handle_open_websocket(websocket):
    all_players[websocket] = Client(websocket)


async def handle_close_websocket(websocket):
    pl = get_client_by_websocket(websocket)
    for code, session in all_sessions.items():
        if session.gm == pl:
            await session.close()
        elif pl in session.players:
            session.players.remove(pl)
            await session.update_session()
    all_players.pop(websocket, None)


HANDLERS = {
    Command.KEEP_ALIVE.value: handle_keep_alive,
    Command.CREATE_SESSION.value: handle_create_session,
    Command.ADD_CARD_SET.value: handle_add_card_set,
    Command.JOIN.value: handle_join_session,
    Command.SET_READY.value: handle_client_ready,
    Command.PICK_CARD.value: handle_pick_card,
    Command.SESSION_STATE.value: handle_session_state
}


def start_everything():
    random.seed()
    threading.Thread(target=partial(http_server.start_webserver, HOST, HTTP_PORT)).start()
    threading.Thread(target=partial(start_websocket, HOST, WEBSOCKET_PORT, handle_open_websocket,
                                    handle_close_websocket, HANDLERS)).start()


if __name__ == '__main__':
    start_everything()
