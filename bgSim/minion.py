from bgSim.deathrattles import get_deathrattle
from bgSim.staticEffects import get_static_effect
from bgSim.personalEffects import get_personal_effect

class Minion:
    def __init__(self, specs):
        self.id = specs["Id"]
        
        self.name = specs["Name"]
        self.tier = specs["Tier"]
        self.tribe = specs["Tribe"]
        self.baseAttack = specs["Attack"]
        self.attack = specs["Attack"]
        self.baseHealth = specs["Health"]
        self.health = specs["Health"]
        self.currentHealth = specs["Health"]
        self.isGolden = False
        
        self.hasTaunt = specs["Taunt"]
        self.hasPoisonous = specs["Poison"]
        self.hasDivineShield = specs["Shield"]
        
        
        self.hasAttacked = False
        self.isDead = False
        
        self.parentMinions = None
        
        self.onHitEffects = []
        self.onHitTriggers = []
        
        self.deathrattles = []
        self.staticEffects = []
        self.personalEffects = []
        
        self.buffs = []
        
        self.abilities = self._set_initial_abilities(specs)
        self.boardNumber = None
        
        self.location = None
    
    def isTribe(self, tribeToCheck):
        """
            Returns True if requested type matches minion type, or minion type is ALL
        """
        if self.tribe == tribeToCheck or self.tribe == "All":
            result = True
        else:
            result = False
        
        return result
    
    
    def get_on_hit_triggers(self):
        toReturn = self.onHitTriggers
        self.onHitTriggers = []
        return toReturn
    
    
    def _set_initial_abilities(self, specs):
        if specs["Deathrattle"]:
            self.deathrattles.append(get_deathrattle(specs["Deathrattle"])(self))
        if specs["StaticEffect"]:
            self.staticEffects.append(get_static_effect(specs["StaticEffect"])(self))
        if specs["PersonalEffect"]:
            self.staticEffects.append(get_personal_effect(specs["PersonalEffect"])(self))
    
    
    def set_board_number(self, number):
        self.boardNumber = number
    
    
    def receive_attack(self, attackingMinion):
        if self.hasDivineShield:
            if attackingMinion.attack > 0:
                self.hasDivineShield = False
        else:
            startHealth = self.currentHealth
            self.currentHealth -= attackingMinion.attack
            if self.currentHealth < startHealth:
                self.onHitTriggers = [x for x in self.personalEffects if x.effectType == "on_damage"]
                if attackingMinion.hasPoisonous:
                    if attackingMinion.attack > 0:
                        self.isDead = True
                if self.currentHealth <= 0:
                    self.isDead = True
    
    
    def update_stats(self):
        attackBuffs = [x.value for x in self.buffs if x.stat == "attack"]
        self.attack = self.baseAttack + sum(attackBuffs)
        
