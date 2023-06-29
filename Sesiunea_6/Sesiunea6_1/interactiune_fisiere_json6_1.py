""""
Practica sesiunea 6_1 -  Interactiunea cu fisiere JSON
"""
import json

"""
JSON = Javascript Object Notation
"""


def citire_din_fisier_json(cale_fisier):
    with open(cale_fisier, 'r') as file:
        return json.load(file)


data = citire_din_fisier_json("quiz.json")
print(type(data))
sport_question = data["quiz"]["sport"]["q1"]["question"]
print(sport_question)


def scriere_in_fisier_json(cale_fisier, randuri_informatii):
    with open(cale_fisier, 'w') as file:
        json.dump(randuri_informatii, file, indent=2)
