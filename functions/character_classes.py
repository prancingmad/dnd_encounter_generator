class BaseClass:
    def __init__(self, level):
        self.level = level

    def get_combat_value(self):
        pass

    def to_dict(self):
        pass

class Artificer(BaseClass):
    def __init__(self, level, primary):
        super().__init__(level)
        self.name = "Artificer"
        self.primary = primary

class Barbarian(BaseClass):
    def __init__(self, level, primary):
        super().__init__(level)
        self.name = "Barbarian"
        self.primary = primary

class Bard(BaseClass):
    def __init__(self, level, primary):
        super().__init__(level)
        self.name = "Bard"
        self.primary = primary

class Cleric(BaseClass):
    def __init__(self, level, primary):
        super().__init__(level)
        self.name = "Cleric"
        self.primary = primary

class Druid(BaseClass):
    def __init__(self, level, primary):
        super().__init__(level)
        self.name = "Druid"
        self.primary = primary

class Fighter(BaseClass):
    def __init__(self, level, primary):
        super().__init__(level)
        self.name = "Fighter"
        self.primary = primary

class Monk(BaseClass):
    def __init__(self, level, primary):
        super().__init__(level)
        self.name = "Monk"
        self.primary = primary

class Paladin(BaseClass):
    def  __init__(self, level, primary):
        super().__init__(level)
        self.name = "Paladin"
        self.primary = primary

class Ranger(BaseClass):
    def __init__(self, level, primary):
        super().__init__(level)
        self.name = "Ranger"
        self.primary = primary

class Rogue(BaseClass):
    def __init__(self, level, primary):
        super().__init__(level)
        self.name = "Rogue"
        self.primary = primary

class Sorcerer(BaseClass):
    def __init__(self, level, primary):
        super().__init__(level)
        self.name = "Sorcerer"
        self.primary = primary

class Warlock(BaseClass):
    def __init__(self, level, primary):
        super().__init__(level)
        self.name = "Warlock"
        self.primary = primary

class Wizard(BaseClass):
    def __init__(self, level, primary):
        super().__init__(level)
        self.name = "Wizard"
        self.primary = primary
