class Monster():
    def __init__(self, name, creature_type, ac, hp, modifiers, num_actions, challenge_rating, num_resist=0, num_immune=0, num_weak=0, is_spellcaster=False, legendary_actions=0):
        self.name = name
        self.creature_type = creature_type
        self.ac = ac
        self.hp = hp
        self.modifiers = modifiers
        self.num_actions = num_actions
        self.challenge_rating = challenge_rating
        self.num_resist = num_resist
        self.num_immune = num_immune
        self.num_weak = num_weak
        self.is_spellcaster = is_spellcaster
        self.legendary_actions = legendary_actions

    def calculate_modifiers(self, stats_dict):
        total = 0
        for stat, score in stats_dict.items():
            total += (score - 10) // 2
        self.modifiers = total
        return total

    def to_dict(self):
        enemy_dict = {}
        enemy_dict["name"] = self.name
        enemy_dict["creature_type"] = self.creature_type
        enemy_dict["ac"] = self.ac
        enemy_dict["hp"] = self.hp
        enemy_dict["modifiers"] = self.modifiers
        enemy_dict["num_resist"] = self.num_resist
        enemy_dict["num_immune"] = self.num_immune
        enemy_dict["num_weak"] = self.num_weak
        enemy_dict["is_spellcaster"] = self.is_spellcaster
        enemy_dict["num_actions"] = self.num_actions
        enemy_dict["legendary_actions"] = self.legendary_actions
        return enemy_dict