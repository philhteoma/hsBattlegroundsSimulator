class PersonalEffect:
    name = "Unnamed Personal Effect"
    def __init__(self, owner):
        self.ownerId = owner.id


class PersonalMinionEnters(PersonalEffect):
    pass


class PersonalAnthem(PersonalEffect):
    pass


class PersonalOnDamage(PersonalEffect):
    effectType = "on_damage"
    pass


class PersonalOther(PersonalEffect):
    pass
    

class PersonalOnAttack(PersonalEffect):
    pass


class PersonalMinionDies(PersonalEffect):
    pass


class PersonalOverkill(PersonalEffect):
    pass


class PersonalOnKill(PersonalEffect):
    pass
    



classList = [
    ]

personalEffects = {x.name: x for x in classList}

def get_personal_effect(name):
    return personalEffects[name]
