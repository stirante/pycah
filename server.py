import asyncio
import mimetypes
import os
import random
import string
import threading
from enum import Enum

import websockets
import http.server
import socketserver
import json
import uuid

from cardcast import CardSet

HOST = "localhost"
HTTP_PORT = 80
WEBSOCKET_PORT = 8080
CACHE = []


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

    async def send(self, packet):
        await self.websocket.send(json.dumps(packet))


class GameSession:
    def __init__(self, gm):
        self.gm = gm
        self.players = []
        self.code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        self.sets = []

    async def broadcast(self, packet):
        for player in self.players:
            await player.send(packet)

    async def send_to_gm(self, packet):
        await self.gm.send(packet)


all_players = {}
all_games = {}


def get_player_by_websocket(websocket):
    for socket, p in all_players.items():
        if websocket == socket:
            return p
    return None


def get_session_by_client(client):
    for code, session in all_games.items():
        if session.gm == client:
            return session
    return None


async def handle_undefined_packet(client, packet):
    pass


async def handle_keep_alive(client, packet):
    pass
    # print("Keep alive:", packet["time"])


async def handle_create_session(client, packet):
    print("Create session")
    session = GameSession(client)
    all_games[session.code] = session
    client.is_player = False
    await client.send({
        "command": Command.CREATE_SESSION.value,
        "client_id": client.client_id,
        "code": session.code
    })


async def handle_add_card_set(client, packet):
    print("Add card set " + packet.set_id)
    session = get_session_by_client(client)
    try:
        set = CardSet(packet.set_id)
        session.sets.append(set)
        await client.send({
            "command": Command.ADD_CARD_SET.value,
            "success": True,
            "set_name": set.name
        })
    except IOError:
        await client.send({
            "command": Command.ADD_CARD_SET.value,
            "success": False
        })


HANDLERS = {
    Command.KEEP_ALIVE.value: handle_keep_alive,
    Command.CREATE_SESSION.value: handle_create_session,
    Command.ADD_CARD_SET.value: handle_add_card_set
}


async def websocket_handler(websocket, path):
    print("Client connection at " + websocket.host)
    all_players[websocket] = Client(websocket)
    try:
        while True:
            data = await websocket.recv()
            packet = json.loads(data)
            handler = HANDLERS.get(packet["command"], handle_undefined_packet)
            await handler(get_player_by_websocket(websocket), packet)
    except websockets.ConnectionClosed:
        print("Connection closed at " + websocket.host)
        pl = get_player_by_websocket(websocket)
        for code, session in all_games.items():
            if session.gm == pl:
                await session.broadcast({
                    "command": Command.GAME_STATE,
                    "game_phase": GamePhase.NOT_JOINED.value,
                    "deck": []
                })
            elif pl in session.players:
                session.players.remove(pl)
        all_players.pop(websocket, None)


class SimpleHTTPServer(http.server.BaseHTTPRequestHandler):
    def _set_headers(self, type):
        self.send_response(200)
        self.send_header('Content-type', type)
        self.end_headers()

    def _send_text(self, text):
        self.wfile.write(bytes(text, "utf-8"))

    def _not_found(self):
        self.send_response(404)
        self.end_headers()

    def _method_not_allowed(self):
        self.send_response(405)
        self.end_headers()

    def do_request(self, only_headers):
        if str.startswith(self.path, "/static/") and os.path.exists('templates' + self.path):
            self._set_headers(mimetypes.guess_type('templates' + self.path)[0])
        elif str.startswith(self.path, "/player.html"):
            self._set_headers(mimetypes.guess_type('templates/player.html'))
        elif str.startswith(self.path, "/desktop.html"):
            self._set_headers(mimetypes.guess_type('templates/desktop.html'))
        elif str.startswith(self.path, "/"):
            self._set_headers(mimetypes.guess_type('templates/index.html'))
        else:
            self._not_found()
            return
        if not only_headers:
            if str.startswith(self.path, "/static/"):
                with open('templates' + self.path, 'r') as file:
                    self._send_text(file.read())
            elif str.startswith(self.path, "/player.html"):
                with open('templates/player.html', 'r') as file:
                    self._send_text(file.read())
            elif str.startswith(self.path, "/desktop.html"):
                with open('templates/desktop.html', 'r') as file:
                    self._send_text(file.read())
            elif str.startswith(self.path, "/"):
                with open('templates/index.html', 'r') as file:
                    self._send_text(file.read())

    def do_GET(self):
        self.do_request(False)

    def do_HEAD(self):
        self.do_request(True)

    def do_POST(self):
        self._method_not_allowed()


def start_webserver():
    with socketserver.TCPServer(("", HTTP_PORT), SimpleHTTPServer) as httpd:
        print("HTTP server started at http://" + HOST + ":" + str(HTTP_PORT) + "/")
        httpd.serve_forever()


def start_websocket():
    asyncio.set_event_loop(asyncio.new_event_loop())
    start_server = websockets.serve(websocket_handler, HOST, WEBSOCKET_PORT)
    asyncio.get_event_loop().run_until_complete(start_server)
    print("Websocket started at ws://" + HOST + ":" + str(WEBSOCKET_PORT) + "/")
    asyncio.get_event_loop().run_forever()


def start_everything():
    threading.Thread(target=start_webserver).start()
    threading.Thread(target=start_websocket).start()


if __name__ == '__main__':
    start_everything()
