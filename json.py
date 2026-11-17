import json

with open("notes.json", "w", encoding ="utf-8") as fil:
    json.dump("hello world ööööööööööööö", fil)