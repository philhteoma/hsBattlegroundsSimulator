
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
    
    
    def get_buff(self, manager):
        return AttackBuff("anthem", 1)


class DireWolfAlphaSeGold(AnthemEffect):
    name = "dire_wolf_alpha_se_gold"
    text = "Adjacent minions have +2 Attack."
    
    def __init__(self, minion):
        self.minionId = minion
        self.minion = minion
        
        self.attackBuff = 1
        self.condition = lambda minion: minion.location in [self.minion.location + 1, self.minion.location - 1]
    
    
    def get_buff(self, manager):
        return AttackBuff("anthem", 2)


class MurlocWarleaderSe(AnthemEffect):
    name = "murloc_warleader_se"
    text = "Your other Murlocs have +2 Attack."
    
    def __init__(self, minion):
        self.minionId = minion
        self.minion = minion
        
        self.condition = lambda minion: minion.isTribe("Murloc") & minion.id != self.minionId
    
    
    def get_buff(self, manager):
        return AttackBuff("anthem", 2)


class MurlocWarleaderSeGold(AnthemEffect):
    name = "murloc_warleader_se_gold"
    text = "Your other Murlocs have +4 Attack."
    
    def __init__(self, minion):
        self.minionId = minion
        self.minion = minion
        self.condition = lambda minion: minion.isTribe("Murloc") & minion.id != self.minionId
    
    
    def get_buff(self, manager):
        return AttackBuff("anthem", 4)


class OldMurkeyeSe(AnthemEffect):
    name = "old_murkeye_se"
    text = "Has +1 attack for each other Murloc on the battlefield."
    
    def __init__(self, minion):
        self.minionId = minion
        self.minion = minion
        self.condition = lambda minion: minion.id == self.minionId
        
        
    def get_buff(self, manager):
        boardOneMurlocs = len(filter(lambda minion: minion.isTribe("Murloc"), manager.get_player_board(1)))
        boardTwoMurlocs = len(filter(lambda minion: minion.isTribe("Murloc"), manager.get_player_board(2)))
        
        buffValue = boardOneMurlocs + boardTwoMurlocs - 1 # Reduce by one as old Murkeye won't count itself
        return AttackBuff("anthem", buffValue)


class OldMurkeyeSeGold(AnthemEffect):
    name = "old_murkeye_se_gold"
    text = "Has +2 attack for each other Murloc on the battlefield."
    
    def __init__(self, minion):
        self.minionId = minion
        self.minion = minion
        self.condition = lambda minion: minion.id == self.minionId
        
        
    def get_buff(self, manager):
        boardOneMurlocs = len(filter(lambda minion: minion.isTribe("Murloc"), manager.get_player_board(1)))
        boardTwoMurlocs = len(filter(lambda minion: minion.isTribe("Murloc"), manager.get_player_board(2)))
        
        buffValue = boardOneMurlocs + boardTwoMurlocs - 1 # Reduce by one as old Murkeye won't count itself
        buffValue *= 2
        return AttackBuff("anthem", buffValue)
        
        

classList = [
    DireWolfAlphaSe,
    DireWolfAlphaSeGold,
    MurlocWarleaderSe,
    MurlocWarleaderSeGold,
    OldMurkeyeSe,
    OldMurkeyeSeGold,
    ]

staticEffects = {x.name: x for x in classList}

def get_static_effect(name):
    return staticEffects[name]
