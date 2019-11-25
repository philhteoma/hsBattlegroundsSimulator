from bgSim.buffs import AttackBuff

class StaticEffect:
    pass


class AnthemEffect(StaticEffect):
    effectType="anthem"


class DeathEffect(StaticEffect):
    pass
    

class AttackEffect(StaticEffect):
    pass


class SummonEffect(StaticEffect):
    pass


class OtherEffect(StaticEffect):
    pass
    

class DireWolfAlphaSe(AnthemEffect):
    name = "dire_wolf_alpha_se"
    text = "Adjacent minions have +1 Attack."
    
    def __init__(self, minion):
        self.minionId = minion
        self.minion = minion
        
        self.attackBuff = 1
        self.condition = lambda minion: minion.location in [self.minion.location + 1, self.minion.location - 1]
    
    
    def get_buff(self):
        return AttackBuff("anthem", 1)


classList = [
    DireWolfAlphaSe,
    ]

staticEffects = {x.name: x for x in classList}

def get_static_effect(name):
    return staticEffects[name]
