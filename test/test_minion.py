from bgSim.minion import Minion


def get_minion_specs(**kwargs):
    defaultMinionSpecs = {
            "Id" : 1,
            "Name" : "TestMinion",
            "Tier" : 1,
            "Tribe" : None,
            "Attack" : 1,
            "Health" : 1,
            "Taunt" : False,
            "Poison" : False,
            "Shield" : False,
            "Deathrattle" : "",
            "StaticEffect" : "",
            "PersonalEffect" : "",
            "Token" : False,
            }

    for key in defaultMinionSpecs.keys():
        if key in kwargs:
            defaultMinionSpecs[key] = kwargs[key]
    
    return defaultMinionSpecs


def test_isTribe():
    neutral = Minion(get_minion_specs())
    murloc = Minion(get_minion_specs(**{"Tribe" : "Murloc"}))
    demon = Minion(get_minion_specs(**{"Tribe" : "Demon"}))
    beast = Minion(get_minion_specs(**{"Tribe" : "Beast"}))
    mech = Minion(get_minion_specs(**{"Tribe" : "Mech"}))
    all = Minion(get_minion_specs(**{"Tribe" : "All"}))
    
    assert(neutral.isTribe("Mech") == False)
    assert(neutral.isTribe("Beast") == False)
    assert(neutral.isTribe("All") == False)
    
    assert(murloc.isTribe("Murloc"))
    assert(murloc.isTribe("Mech") == False)
    assert(murloc.isTribe("All") == False)
    
    assert(demon.isTribe("Demon"))
    assert(demon.isTribe("Mech") == False)
    assert(demon.isTribe("All") == False)

    assert(beast.isTribe("Beast"))
    assert(beast.isTribe("Mech") == False)
    assert(beast.isTribe("All") == False)

    assert(mech.isTribe("Mech"))
    assert(mech.isTribe("Demon") == False)
    assert(mech.isTribe("All") == False)

    assert(all.isTribe("Murloc"))
    assert(all.isTribe("Demon"))
    assert(all.isTribe("Beast"))
    assert(all.isTribe("Mech"))
    assert(all.isTribe("All"))
    
    
def test_get_on_hit_triggers():
    pass


def test_set_board_number():
    minion = Minion(get_minion_specs())
    
    minion.set_board_number(1)
    
    assert(minion.boardNumber == 1)
    assert(minion.boardNumber != 2)


def test_receive_attack_simple():
    minionOne = Minion(get_minion_specs(**{"Attack" : 1, "Health" : 3}))
    minionTwo = Minion(get_minion_specs(**{"Attack" : 2, "Health" : 1}))
    
    minionOne.receive_attack(minionTwo)
    
    assert(minionOne.currentHealth == 1)
    assert(minionOne.isDead == False)
    assert(minionTwo.currentHealth == 1)
    assert(minionTwo.isDead == False)

    minionTwo.receive_attack(minionOne)
    
    assert(minionOne.currentHealth == 1)
    assert(minionOne.isDead == False)
    assert(minionTwo.currentHealth == 0)
    assert(minionTwo.isDead)
    
    assert(minionOne.maxHealth == 3)
    assert(minionTwo.maxHealth == 1)


def test_receive_poison_attack():
    normalMinion = Minion(get_minion_specs(**{"Attack" : 1, "Health" : 999}))
    poisonMinion = Minion(get_minion_specs(**{"Attack" : 1, "Health" : 1, "Poison" : True}))
    
    normalMinion.receive_attack(poisonMinion)
    
    assert(normalMinion.currentHealth == 998)
    assert(normalMinion.isDead)
    

def test_divine_shield():
    strongMinion = Minion(get_minion_specs(**{"Attack" : 100, "Health" : 10}))
    poisonMinion = Minion(get_minion_specs(**{"Attack" : 1, "Health" : 1, "Poison" : True}))
    weakMinion = Minion(get_minion_specs(**{"Attack" : 0, "Health" : 10}))
    
    shieldMinion = Minion(get_minion_specs(**{"Attack" : 1, "Health" : 10, "Shield" : True}))
    assert(shieldMinion.hasDivineShield)
    
    shieldMinion.receive_attack(strongMinion)
    assert(shieldMinion.currentHealth == 10)
    assert(shieldMinion.hasDivineShield == False)
    assert(shieldMinion.isDead == False)
    
    shieldMinionTwo  = Minion(get_minion_specs(**{"Attack" : 1, "Health" : 10, "Shield" : True}))
    assert(shieldMinionTwo.hasDivineShield)
    
    shieldMinionTwo.receive_attack(poisonMinion)
    assert(shieldMinionTwo.currentHealth == 10)
    assert(shieldMinionTwo.hasDivineShield == False)
    assert(shieldMinionTwo.isDead == False)
    
    shieldMinionThree = Minion(get_minion_specs(**{"Attack" : 1, "Health" : 10, "Shield" : True}))
    assert(shieldMinionThree.hasDivineShield)
    
    shieldMinionThree.receive_attack(weakMinion)
    assert(shieldMinionThree.currentHealth == 10)
    assert(shieldMinionThree.hasDivineShield == True)
    assert(shieldMinionThree.isDead == False)

    
    
