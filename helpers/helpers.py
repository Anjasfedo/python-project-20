import json

def readJson(path, value):
    with open(path, "r") as configs:
        config = json.load(configs)
        return config[value]
