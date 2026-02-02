import json
import requests

with open("whitelist.json") as file:
    list = json.load(file)
    for l in list:
        name = l["name"]
        s = requests.Session()
        r = s.get(f"https://mc-heads.net/avatar/{name}")

        with open(f"icons/{name}.png", mode="wb") as file:
            file.write(r.content)
