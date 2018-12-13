import json

import requests

_CARDCAST_BASE_URL = "https://api.cardcastgame.com/v1/decks/"


class CardSet:
    def __init__(self, code):
        info = json.loads(requests.get(_CARDCAST_BASE_URL + code))
        self.name = info["name"]
        cards = json.loads(requests.get(_CARDCAST_BASE_URL + code + "/cards"))
        self.questions = []
        self.answers = []
        for question in cards["calls"]:
            if len(question["text"]) == 2:
                self.questions.append("___".join(question["text"]))
        for answer in cards["responses"]:
            self.answers.append(answer["text"][0])
