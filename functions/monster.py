from .config import *

class Monster():
    def __init__(self, name, challenge_rating):
        self.name = name
        self.challenge_rating = challenge_rating

    def to_dict(self):
        enemy_dict = {}
        enemy_dict["name"] = self.name
        enemy_dict["challenge_rating"] = self.challenge_rating
        return enemy_dict

    def save_to_file(self):
        monster_list = []
        if os.path.exists(PARTY_FILE_PATH):
            with open(PARTY_FILE_PATH, "r") as f:
                content = f.read().strip()
                if content:
                    players_list = json.loads(content)
        player_dict = self.to_dict()
        players_list.append(player_dict)
        with open(PARTY_FILE_PATH, "w") as f:
            json.dump(players_list, f, indent=4)