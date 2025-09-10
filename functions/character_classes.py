from config import *

class BaseClass:
    def __init__(self, name, level, mod):
        self.name = name
        self.level = level
        self.mod = mod

    def get_combat_value(self):
        return self.level * self.mod

class Artificer(BaseClass):
    def __init__(self, level, primary):
        super().__init__("Artificer", level, ARTI_MOD)
        self.primary = primary

class Barbarian(BaseClass):
    def __init__(self, level, primary):
        super().__init__("Barbarian", level, BARB_MOD)
        self.primary = primary

class Bard(BaseClass):
    def __init__(self, level, primary):
        super().__init__("Bard", level, BARD_MOD)
        self.primary = primary

class Cleric(BaseClass):
    def __init__(self, level, primary):
        super().__init__("Cleric", level, CLER_MOD)
        self.primary = primary

class Druid(BaseClass):
    def __init__(self, level, primary):
        super().__init__("Druid", level, DRUI_MOD)
        self.primary = primary

class Fighter(BaseClass):
    def __init__(self, level, primary):
        super().__init__("Fighter", level, FIGH_MOD)
        self.primary = primary

class Monk(BaseClass):
    def __init__(self, level, primary):
        super().__init__("Monk", level, MONK_MOD)
        self.primary = primary

class Paladin(BaseClass):
    def  __init__(self, level, primary):
        super().__init__("Paladin", level, PALA_MOD)
        self.primary = primary

class Ranger(BaseClass):
    def __init__(self, level, primary):
        super().__init__("Ranger", level, RANG_MOD)
        self.primary = primary

class Rogue(BaseClass):
    def __init__(self, level, primary):
        super().__init__("Rogue", level, ROGU_MOD)
        self.primary = primary

class Sorcerer(BaseClass):
    def __init__(self, level, primary):
        super().__init__("Sorcerer", level, SORC_MOD)
        self.primary = primary

class Warlock(BaseClass):
    def __init__(self, level, primary):
        super().__init__("Warlock", level, WARL_MOD)
        self.primary = primary

class Wizard(BaseClass):
    def __init__(self, level, primary):
        super().__init__("Wizard", level, WIZA_MOD)
        self.primary = primary