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


class DireWolfAlphaSeGold(AnthemEffect):
    name = "dire_wolf_alpha_se_gold"
    text = "Adjacent minions have +2 Attack."
    
    def __init__(self, minion):
        self.minionId = minion
        self.minion = minion
        
        self.attackBuff = 1
        self.condition = lambda minion: minion.location in [self.minion.location + 1, self.minion.location - 1]
    
    
    def get_buff(self):
        return AttackBuff("anthem", 2)


class MurlocWarleaderSe(AnthemEffect):
    name = "murloc_warleader_se"
    text = "Your other Murlocs have +2 Attack."
    
    def __init__(self, minion):
        self.minionId = minion
        self.minion = minion
        
        self.attackBuff = 1
        self.condition = lambda minion: minion.isTribe("Murloc") & minion.id != self.minionId
    
    
    def get_buff(self):
        return AttackBuff("anthem", 2)


class MurlocWarleaderSeGold(AnthemEffect):
    name = "murloc_warleader_se_gold"
    text = "Your other Murlocs have +4 Attack."
    
    def __init__(self, minion):
        self.minionId = minion
        self.minion = minion
        
        self.attackBuff = 1
        self.condition = lambda minion: minion.isTribe("Murloc") & minion.id != self.minionId
    
    
    def get_buff(self):
        return AttackBuff("anthem", 4)


classList = [
    DireWolfAlphaSe,
    DireWolfAlphaSeGold,
    MurlocWarleaderSe,
    MurlocWarleaderSeGold,
    ]

staticEffects = {x.name: x for x in classList}

def get_static_effect(name):
    return staticEffects[name]
