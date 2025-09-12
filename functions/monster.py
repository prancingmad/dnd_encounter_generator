class Monster():
    def __init__(self, name, challenge_rating):
        self.name = name
        self.challenge_rating = challenge_rating

    def to_dict(self):
        enemy_dict = {}
        enemy_dict["name"] = self.name
        enemy_dict["challenge_rating"] = self.challenge_rating
        return enemy_dict