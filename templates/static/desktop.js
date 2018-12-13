let wsocket = new WebSocket("ws://localhost:8080/");
wsocket.onmessage = evt => {
    console.log(evt.data);
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
    code: null,
    players: []
};

function handleCreateSessionResponse(packet) {
    LocalSession.clientId = packet.client_id;
    LocalSession.code = packet.code;
    //$("#create-session").css("display", "none");
    let $code = $("#code");
    $code.text(LocalSession.code);
    $code.css("display", "block");
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
    LocalSession.players = packet.players;
    if (LocalSession.gamePhase === SessionPhase.NOT_STARTED) {
        let ready = 0;
        for (let player in LocalSession.players) {
            if (player.ready) ready++;
        }
        let count = "Ready players: " + ready + "/" + LocalSession.players.length;
        if (LocalSession.players.length < 2) count += " (Minimum 2 players required)";
        $("#pregame-player-count").text(count);
    }
}

function keepAlive() {
    wsocket.send(JSON.stringify({command: Command.KEEP_ALIVE, time: Date.now().valueOf()}));
    setTimeout(keepAlive, 10000);
}

function createSession() {
    let $create = $("#create-session");
    $create.addClass("fade-out");
    afterAnimation(() => {
        $("#create-session").css("display", "none");
        if (LocalSession.code !== null) {
            let $codeContainer = $("#code-container");
            let $code = $("#code");
            $code.text(LocalSession.code);
            $codeContainer.css("display", "block");
            setTimeout(() =>
                $codeContainer.removeClass("fade-out"), 10);
        }
    });
    wsocket.send(JSON.stringify({command: Command.CREATE_SESSION}));
}

function addCardSet(id) {
    wsocket.send(JSON.stringify({command: Command.PICK_CARD, client_id: LocalSession.clientId, set_id: id}));
}

function afterAnimation(func) {
    setTimeout(func, 300);
}