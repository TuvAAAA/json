import json

filename = "user_config.json"


def read_in(): 
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
    
        return[]

    