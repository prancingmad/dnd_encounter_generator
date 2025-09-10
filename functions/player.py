class Player():
    def __init__(self, armor_class, magic_items):
        self.armor_class = armor_class
        self.magic_items = magic_items


# placeholder

combat_value = 0
        arti_level = sum(cls.level for cls in self.classes if cls.name == "Artificer") * ARTI_MOD
        barb_level = sum(cls.level for cls in self.classes if cls.name == "Barbarian") * BARB_MOD
        bard_level = sum(cls.level for cls in self.classes if cls.name == "Bard") * BARD_MOD
        cler_level = sum(cls.level for cls in self.classes if cls.name == "Cleric") * CLER_MOD
        drui_level = sum(cls.level for cls in self.classes if cls.name == "Druid") * DRUI_MOD
        figh_level = sum(cls.level for cls in self.classes if cls.name == "Fighter") * FIGH_MOD
        monk_level = sum(cls.level for cls in self.classes if cls.name == "Monk") * MONK_MOD
        pala_level = sum(cls.level for cls in self.classes if cls.name == "Paladin") * PALA_MOD
        rang_level = sum(cls.level for cls in self.classes if cls.name == "Ranger") * RANG_MOD
        rogu_level = sum(cls.level for cls in self.classes if cls.name == "Rogue") * ROGU_MOD
        sorc_level = sum(cls.level for cls in self.classes if cls.name == "Sorcerer") * SORC_MOD
        warl_level = sum(cls.level for cls in self.classes if cls.name == "Warlock") * WARL_MOD
        wiza_level = sum(cls.level for cls in self.classes if cls.name == "Wizard") * WIZA_MOD
        if barb_level >= 5 or figh_level >= 5 or monk_level >= 5 or pala_level >= 5 or rang_level >= 5:
            combat_value += EXTRA_ATTACK_MOD
        if barb_level >= 2:
            combat_value += RECKLESS_MOD
        if pala_level >= 2:
            combat_value += SMITE_MOD
        if figh_level >= 2:
            combat_value += SURGE_MOD
        if rogu_level >= 1:
            combat_value += SNEAK_MOD
        if monk_level >= 5:
            combat_value += STUN_STRIKE_MOD
        return combat_value + arti_level + barb_level + bard_level + cler_level + drui_level + figh_level + monk_level + pala_level + rang_level + sorc_level + warl_level + wiza_level