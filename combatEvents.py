import random

class CombatEvent:
    def __init__(self, manager):
        self.manager = manager


class ChooseAttackTarget(CombatEvent):
    name = "choose_attack_target"
    super().__init__()
        
    
    def run(self):
        self.manager.attackingMinion = self.manager.get_active_board().get_leftmost_minion()
        attackableTargets = self.manager.get_inactive_board().get_attackable_targets()
        self.manager.defendingMinion = random.choice(attackableTargets)
        self.manager.combatStack.append(Fight(self.manager))
    

class Fight(CombatEvent):
    name = "fight"
    super().__init__()
    
    def run(self):
        self.manager.defendingMinion.recieveAttack(self.manager.attackingMinion)
        self.manager.attackingMinion.recieveAttack(self.manager.defendingMinion)
        onHitEffects = [self.manager.attackingMinion.get_on_hit_triggers()] + [self.manager.defendingMinion.get_on_hit_triggers()]
        if onHitEffects:
            pass
        


classList = [
    ChooseAttackTarget,
    Fight,
    ]

combatEvents = {x.name: x for x in classList}


def get_combat_event(name):
    return combatEvents[name]
    
