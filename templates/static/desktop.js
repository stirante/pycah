let wsocket = new WebSocket("ws://" + location.host + ":8080/");
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

function switchContainers(a, b) {
    $("#" + a).addClass("fade-out");
    setTimeout(function () {
        $("#" + a).css("display", "none");
        $("#" + b).css("display", "block");
        setTimeout(function () {
            $("#" + b).removeClass("fade-out");
        }, 10);
    }, 300);
}

function handleCreateSessionResponse(packet) {
    LocalSession.clientId = packet.client_id;
    LocalSession.code = packet.code;
    let $code = $("#code");
    $code.text(LocalSession.code);
    let $invite = $("#invite-qr-code");
    $invite.click(() => {
        let win = window.open("http://" + location.hostname + "/player.html#" + LocalSession.code, "_blank");
        if (win) {
            win.focus();
        } else {
            alert("Please allow popups for this website");
        }
    });
    new QRCode($invite[0], {
        text: "http://" + location.hostname + "/player.html#" + LocalSession.code,
        width: 128,
        height: 128,
        colorDark: "#000000",
        colorLight: "#ffffff",
        correctLevel: QRCode.CorrectLevel.L
    });
}

function handleAddCardSetResponse(packet) {
    if (!packet.success) {
        alert("Failed to add card set " + packet.set_id);
    } else {
        alert("Card set \"" + packet.set_name + "\" added successfully")
    }
}

function handleSessionState(packet) {
    let oldPhase = LocalSession.gamePhase;
    LocalSession.gamePhase = packet.game_phase;
    LocalSession.question = packet.question;
    LocalSession.answers = packet.answers;
    LocalSession.highlight = packet.highlight;
    LocalSession.players = packet.players;
    if (LocalSession.gamePhase === SessionPhase.NOT_STARTED) {
        let ready = 0;
        for (let player in LocalSession.players) {
            if (LocalSession.players[player].ready) ready++;
        }
        let count = "Ready players: " + ready + "/" + LocalSession.players.length;
        if (LocalSession.players.length < 2) count += " (Minimum 2 players required)";
        $("#pregame-player-count").text(count);
    } else if (LocalSession.gamePhase === SessionPhase.PICK_YOUR_CARD) {
        let $question = $("#question-container");
        $question.empty();
        $question.html(createScoreboard(LocalSession.players) + createQuestionCard(LocalSession.question));
        if (oldPhase === SessionPhase.NOT_STARTED) {
            switchContainers("code-container", "question-container");
        } else {
            switchContainers("answers-container", "question-container");
        }
    } else if (LocalSession.gamePhase === SessionPhase.PICK_BEST_CARD) {
        let $question = $("#question-container");
        let html = createScoreboard(LocalSession.players) + createQuestionCard(LocalSession.question);
        for (let x in LocalSession.answers) {
            html += createAnswerCard(LocalSession.answers[x]);
        }
        $question.html(html);
    } else if (LocalSession.gamePhase === SessionPhase.ROUND_WINNER) {
        let $question = $("#question-container");
        let winner = "";
        if (LocalSession.highlight === "")
            winner = "<div class=\"alert alert-info\">" +
                "This round ended in <strong>draw</strong>!" +
                "  </div>";
        else
            winner = "<div class=\"alert alert-success\">" +
                "Winner of this round is <strong>" + LocalSession.highlight + "</strong>!" +
                "</div>";
        let html = createScoreboard(LocalSession.players) + winner + createQuestionCard(LocalSession.question);
        for (let x in LocalSession.answers) {
            html += createAnswerCard(LocalSession.answers[x]);
        }
        $question.html(html);
        setTimeout(() => {
            wsocket.send(JSON.stringify({
                command: Command.SESSION_STATE,
                client_id: LocalSession.clientId,
                game_phase: SessionPhase.PICK_YOUR_CARD
            }))
        }, 5000);
    }
}

function createScoreboard(players) {
    let table = "<table class='scoreboard table table-bordered'><tr><td>Player</td><td>Score</td></tr>";
    for (let player in players) {
        table += "<tr><td>" + htmlEncode(players[player].username) + "</td><td>" + players[player].score + "</td></tr>"
    }
    return table;
}

function createQuestionCard(text) {
    return "<div class=\"card question-card desktop-card\">" + text + "</div>";
}

function createAnswerCard(text) {
    return "<div class=\"card desktop-card\">" + text + "</div>";
}

function keepAlive() {
    wsocket.send(JSON.stringify({command: Command.KEEP_ALIVE, time: Date.now().valueOf()}));
    setTimeout(keepAlive, 10000);
}

function createSession() {
    wsocket.send(JSON.stringify({command: Command.CREATE_SESSION}));
    switchContainers("create-session", "code-container");
}

function addCardSet(id) {
    $('#card-set-id').val("");
    wsocket.send(JSON.stringify({command: Command.ADD_CARD_SET, client_id: LocalSession.clientId, set_id: id}));
}

function htmlEncode(value) {
    return $('<div/>').text(value).html();
}