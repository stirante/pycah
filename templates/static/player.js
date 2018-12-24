let wsocket = new WebSocket("ws://" + location.host + ":8080/");
wsocket.onmessage = evt => {
    console.log(evt.data);
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

wsocket.onclose = () => {
    alert("Connection closed!");
    //wsocket = new WebSocket("ws://" + location.host + ":8080/");
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
    deck: [],
    picked: false
};

function switchContainers(a, b) {
    $("#" + a).addClass("fade-out");
    setTimeout(() => {
        $("#" + a).css("display", "none");
        $("#" + b).css("display", "block");
        setTimeout(() => {
            $("#" + b).removeClass("fade-out");
        }, 10);
    }, 300);
}

function handleJoinResponse(packet) {
    if (packet.success) {
        LocalPlayer.clientId = packet.client_id;
        LocalPlayer.gamePhase = GamePhase.NOT_STARTED;
        switchContainers("join-container", "ready-container");
    } else {
        alert("Invalid code or username!");
    }
}

function handleGameState(packet) {
    let oldPhase = LocalPlayer.gamePhase;
    LocalPlayer.gamePhase = packet.game_phase;
    LocalPlayer.deck = packet.deck;
    if (LocalPlayer.gamePhase === GamePhase.NOT_JOINED) {
        let $join = $("#join-container");
        $join.css("display", "block");
        $join.removeClass("fade-out");
        $("#ready-container").css("display", "none");
        $("#wait-container").css("display", "none");
        $("#card-container").css("display", "none");
    } else if (LocalPlayer.gamePhase === GamePhase.PICK_YOUR_CARD ||
        LocalPlayer.gamePhase === GamePhase.PICK_BEST_CARD) {
        LocalPlayer.picked = false;
        let deck = "";
        for (let card in LocalPlayer.deck) {
            deck += createAnswerCard(LocalPlayer.deck[card]);
        }
        $("#card-container").html(deck);
        if (oldPhase === GamePhase.NOT_STARTED) {
            // switchContainers("ready-container", "card-container");
            $("#ready-container").addClass("fade-out");
            $("#wait-container").addClass("fade-out");
            setTimeout(() => {
                $("#ready-container").css("display", "none");
                $("#wait-container").css("display", "none");
                $(document.body).css("height", "initial");
                $("#card-container").css("display", "flex");
                setTimeout(() => {
                    $("#card-container").removeClass("fade-out");
                }, 10);
            }, 300);
        }
    }
}

function keepAlive() {
    wsocket.send(JSON.stringify({command: Command.KEEP_ALIVE, time: Date.now().valueOf()}));
    setTimeout(keepAlive, 10000);
}

function joinSession(code, username) {
    wsocket.send(JSON.stringify({command: Command.JOIN, code: code, username: username}));
}

function setReady(isReady) {
    wsocket.send(JSON.stringify({command: Command.SET_READY, client_id: LocalPlayer.clientId, ready: isReady}));
    switchContainers("ready-container", "wait-container");
}

function pickCard(cardId) {
    if (LocalPlayer.picked) return;
    LocalPlayer.picked = true;
    wsocket.send(JSON.stringify({command: Command.PICK_CARD, client_id: LocalPlayer.clientId, card_id: cardId}));
    $(".card").each((index, currentElement) => {
        if ($(currentElement).text() === cardId) return;
        $(currentElement).css("background-color", "#bbbbbb");
    })
}

function createAnswerCard(text) {
    return "<div class=\"col-6 col-md-3\"><div class=\"card\" onclick='pickCard($(this).text())'>" + text + "</div></div>";
}

$(document).ready(() => {
    if (window.location.hash) {
        $("#session-code").val(window.location.hash.substr(1))
    }
});