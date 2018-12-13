let wsocket = new WebSocket("ws://localhost:8080/");
wsocket.onmessage = evt => {
    let packet = JSON.parse(evt.data);
    switch (packet.command) {
        case Command.SESSION_STATE:
            handleSessionState(packet);
            break;
        case Command.CREATE_SESSION:
            handleCreateSessionResponse(packet);
            break;
        case Command.ADD_CARD_SET:
            handleAddCardSetResponse(packet);
            break;
    }
};
wsocket.onopen = () => {
    keepAlive();
};

const Command = {
    KEEP_ALIVE: "keep_alive",
    CREATE_SESSION: "create_session",
    ADD_CARD_SET: "add_card_set",
    // server-side
    SESSION_STATE: "session_state"
};

const SessionPhase = {
    NOT_STARTED: 0,
    PICK_YOUR_CARD: 1,
    PICK_BEST_CARD: 2,
    ROUND_WINNER: 3
};

const LocalSession = {
    clientId: null,
    sessionPhase: SessionPhase.NOT_STARTED,
    question: null,
    answers: [],
    highlight: null,
    code: null
};

function handleCreateSessionResponse(packet) {
    LocalSession.clientId = packet.client_id;
    LocalSession.code = packet.code;
}

function handleAddCardSetResponse(packet) {
    if (!packet.success) {
        alert("Failed to add card set " + packet.set_id);
    }
}

function handleSessionState(packet) {
    LocalSession.gamePhase = packet.game_phase;
    LocalSession.question = packet.question;
    LocalSession.answers = packet.answers;
    LocalSession.highlight = packet.highlight;
}

function keepAlive() {
    wsocket.send(JSON.stringify({command: Command.KEEP_ALIVE, time: Date.now().valueOf()}));
    setTimeout(keepAlive, 10000);
}

function createSession(code) {
    wsocket.send(JSON.stringify({command:Command.CREATE_SESSION}));
}

function addCardSet(id) {
    wsocket.send(JSON.stringify({command: Command.PICK_CARD, client_id: LocalSession.clientId, set_id: id}));
}