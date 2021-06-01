import json

# From https://github.com/crhallberg/json-against-humanity
# Structure:
# {
#     "white": [],
#     "black": [
#         {
#             "text": "text",
#             "pick": 1
#         }
#     ],
#     "packs": [
#         {
#             "name": "name",
#             "official": True,
#             "white": [0, 1, 2],
#             "black": [0, 1, 2]
#         }
#     ]
# }
with open('cah-all-compact.json', 'r', encoding="utf8") as cah_all:
    _CAH_ALL = json.load(cah_all)

_ALL_PACKS = [{"id": x, "name": _CAH_ALL["packs"][x]["name"], "official": _CAH_ALL["packs"][x]["official"]} for x in
              range(len(_CAH_ALL["packs"]))]


class CardSet:
    def __init__(self, index):
        self.name = _CAH_ALL["packs"][index]["name"]
        self.official = _CAH_ALL["packs"][index]["official"]
        self.questions = []
        self.answers = []
        for q in filter(lambda x: _CAH_ALL["black"][x]["pick"] == 1, _CAH_ALL["packs"][index]["black"]):
            self.questions.append(_CAH_ALL["black"][q]["text"])
        for a in _CAH_ALL["packs"][index]["white"]:
            self.answers.append(_CAH_ALL["white"][a])


# Just testing getting cards
if __name__ == '__main__':
    print(json.dumps(_ALL_PACKS))
    s = CardSet(0)
    print(s.name)
    for question in s.questions:
        print("Question: " + question)
    for answer in s.answers:
        print("Answer: " + answer)
