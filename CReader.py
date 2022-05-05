import json


def getResolution(type):
    file = open("Config.json")
    js = json.load(file)
    if type == "h":
        return js['Resolution']['Height']
    if type == "w":
        return js['Resolution']['Width']


def getFaction():
    file = open("Config.json")
    js = json.load(file)
    return js['Faction']
