import random

class CombatEvent:
    pass


class ChooseAttackTarget(CombatEvent):
    name = "choose_attack_target"
    
    def run(self, manager):
        manager.attackingMinion = manager.get_active_board().get_leftmost_minion()
        attackableTargets = manager.get_inactive_board().get_attackable_targets()
        manager.defendingMinion = random.choice(attackableTargets)
        manager.combatStack.append(Fight())
    

class Fight(CombatEvent):
    name = "fight"
    
    def run(self, manager):
        print("Attacking Minion: {} (Player{})".format(manager.attackingMinion.name, manager.get_active_board().boardNumber))
        print("Defending Minion: {} (Player{})".format(manager.defendingMinion.name, manager.get_inactive_board().boardNumber))
        manager.attackingMinion.receive_attack(manager.defendingMinion)
        manager.defendingMinion.receive_attack(manager.attackingMinion)
        onHitEffects = manager.attackingMinion.get_on_hit_triggers() + manager.defendingMinion.get_on_hit_triggers()
        if onHitEffects:
            print(onHitEffects)
            manager.combatStack = onHitEffects + manager.combatStack
        


classList = [
    ChooseAttackTarget,
    Fight,
    ]

combatEvents = {x.name: x for x in classList}


def get_combat_event(name):
    return combatEvents[name]
    
