class StaticEffect:
    pass


class AnthemEffect(StaticEffect):
    pass


class DeathEffect(StaticEffect):
    pass
    

class AttackEffect(StaticEffect):
    pass


class OummonEffect(StaticEffect):
    pass


class OtherEffect(StaticEffect):
    pass
    




class DireWolfAlphaSe(AnthemEffect):
    name = "dire_wolf_alpha_se"
    text = "Adjacent minions have +1 Attack."
    
    def __init__(self, minion):
        self.minionId = minion
        self.minion = minion


classList = [
    DireWolfAlphaSe,
    ]

staticEffects = {x.name: x for x in classList}

def get_static_effect(name):
    return staticEffects[name]
