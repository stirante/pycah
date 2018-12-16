import json

import requests

_CARDCAST_BASE_URL = "https://api.cardcastgame.com/v1/decks/"


class CardSet:
    def __init__(self, code):
        print("Getting code", code)
        info = json.loads(requests.get(_CARDCAST_BASE_URL + code).text)
        self.name = info["name"]
        cards = json.loads(requests.get(_CARDCAST_BASE_URL + code + "/cards").text)
        self.questions = []
        self.answers = []
        for question in cards["calls"]:
            if len(question["text"]) == 2:
                self.questions.append("___".join(question["text"]))
        for answer in cards["responses"]:
            self.answers.append(answer["text"][0])


# Just testing getting cards
if __name__ == '__main__':
    set = CardSet("XFA6T")
    print(set.name)
    for question in set.questions:
        print("Question: " + question)
    for answer in set.answers:
        print("Answer: " + answer)
