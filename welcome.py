import json

filename = "user_config.json"

def read_in(): 
    try:
        with open("data.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return{}

def save_data(data):
  with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2, ensure_ascii=False)