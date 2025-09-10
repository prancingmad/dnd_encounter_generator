import os
import json

party_file_path = os.path.join("information", "party.json")

def remove_party_member(player_name):
    if os.path.exists(party_file_path):
        with open(party_file_path, "r") as f:
            content = f.read().strip()
            if content:
                players_list = json.loads(content)
            else:
                players_list = []

    if players_list == []:
        raise ValueError("Currently party is empty")

    for index, player in enumerate(players_list):
        if player["name"] == player_name:
            players_list.pop(index)
            with open(party_file_path, "w") as f:
                json.dump(players_list, f, indent=4)
            break
    else:
        raise ValueError("Party member not found")
