class Buff:
    pass


class AttackBuff:
    stat = "attack"
    
    def __init__(self, buffType, buffValue):
        self.buffType = buffType
        self.value = buffValue
