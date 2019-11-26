class Buff:
    pass


class AttackBuff(Buff):
    stat = "attack"
    initialBuffUsed = None # Attack shouldn't use this
    
    def __init__(self, buffType, buffValue):
        self.buffType = buffType
        self.value = buffValue


class HealthBuff(Buff):
    stat = "health"
    initialBuffUsed = False
    
    def __init__(self, buffType, buffValue):
        self.buffType = buffType
        self.buffValue = buffValue
