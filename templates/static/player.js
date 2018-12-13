let wsocket = new WebSocket("ws://localhost:8080/");
wsocket.onmessage = evt => {
    let packet = JSON.parse(evt.data);
    switch (packet.command) {
        case Command.JOIN:
            handleJoinResponse(packet);
            break;
        case Command.GAME_STATE:
            handleGameState(packet);
            break;
    }
};
wsocket.onopen = () => {
    keepAlive();
};

const Command = {
    KEEP_ALIVE: "keep_alive",
    JOIN: "join",
    // client-side
    SET_READY: "set_ready",
    PICK_CARD: "pick_card",
    // server-side
    GAME_STATE: "game_state"
};

const GamePhase = {
    NOT_JOINED: -1,
    NOT_STARTED: 0,
    PICK_YOUR_CARD: 1,
    PICK_BEST_CARD: 2,
    ROUND_WINNER: 3
};

const LocalPlayer = {
    clientId: null,
    gamePhase: GamePhase.NOT_JOINED,
    deck: []
};

function handleJoinResponse(packet) {
    if (packet.success) {
        LocalPlayer.clientId = packet.client_id;
        LocalPlayer.gamePhase = GamePhase.NOT_STARTED
    } else {
        alert("Invalid code!");
    }
}

function handleGameState(packet) {
    LocalPlayer.gamePhase = packet.game_phase;
    LocalPlayer.deck = packet.deck;
}

function keepAlive() {
    wsocket.send(JSON.stringify({command: Command.KEEP_ALIVE, time: Date.now().valueOf()}));
    setTimeout(keepAlive, 10000);
}

function joinSession(code) {
    wsocket.send(JSON.stringify({command: Command.JOIN}));
}

function setReady(isReady) {
    wsocket.send(JSON.stringify({command: Command.SET_READY, client_id: LocalPlayer.clientId, ready: isReady}));
}

function pickCard(cardId) {
    wsocket.send(JSON.stringify({command: Command.PICK_CARD, client_id: LocalPlayer.clientId, card_id: cardId}));
}