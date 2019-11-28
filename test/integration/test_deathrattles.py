from bgSim.gameManager import GameManager
from bgSim.minionRepository import MinionRepository
from unittest.mock import MagicMock

deathrattleMinions = [
    "Mecharoo",
    "Selfless Hero",
    "Harvest Golem",
    "Kaboom Bot",
    "Kindly Grandmother",
    "Mounted Raptor",
    "Rat Pack",
    "Spawn of N'Zoth",
    ]


defaultMinion = "Wrath Weaver"
highHealthMinion = "Screwjank Clunker"

csvPath = "static_data/minions.csv"
repo = MinionRepository(csvPath)


def test_mecharoo_dr():
    manager = GameManager(repo)
    manager.set_first_player(1)
    testMinion = manager.create_minion("Mecharoo")
    
    manager.assign_minion_to_board(manager.create_minion(defaultMinion), 1)
    manager.assign_minion_to_board(testMinion, 1)
    manager.assign_minion_to_board(manager.create_minion(defaultMinion), 1)

    boardOne = manager.get_player_board(1)
    assert(boardOne.minions[1] == testMinion)
    
    mockSource = MagicMock()
    mockSource.hasPoisonous = False
    testMinion.recieve_damage(1, mockSource)
    manager.check_for_death()
    manager.combat_substep()
    
    assert(len(boardOne.minions) == 3)
    assert(boardOne.minions[0].name == defaultMinion)
    assert(boardOne.minions[1].name == "Jo-E Bot")
    assert(boardOne.minions[1].isGold == False)
    assert(boardOne.minions[2].name == defaultMinion)
    

def test_gold_mecharoo_dr():
    manager = GameManager(repo)
    manager.set_first_player(1)
    testMinion = manager.create_minion("Mecharoo", isGold=True)
    
    manager.assign_minion_to_board(manager.create_minion(defaultMinion), 1)
    manager.assign_minion_to_board(testMinion, 1)
    manager.assign_minion_to_board(manager.create_minion(defaultMinion), 1)

    boardOne = manager.get_player_board(1)
    assert(boardOne.minions[1] == testMinion)
    assert(boardOne.minions[1].isGold == True)
    
    mockSource = MagicMock()
    mockSource.hasPoisonous = False
    testMinion.recieve_damage(2, mockSource)
    manager.check_for_death()
    manager.combat_substep()
    
    assert(len(boardOne.minions) == 3)
    assert(boardOne.minions[0].name == defaultMinion)
    assert(boardOne.minions[1].name == "Jo-E Bot")
    assert(boardOne.minions[1].isGold == True)
    assert(boardOne.minions[2].name == defaultMinion)
    
    
def test_selfless_hero_dr():
    results = []
    for i in range(100):
        manager = GameManager(repo)
        manager.set_first_player(1)
        testMinion = manager.create_minion("Selfless Hero", isGold=False)
        
        manager.assign_minion_to_board(manager.create_minion(defaultMinion), 1)
        manager.assign_minion_to_board(testMinion, 1)
        manager.assign_minion_to_board(manager.create_minion(defaultMinion), 1)

        boardOne = manager.get_player_board(1)
        assert(boardOne.minions[1] == testMinion)
        assert(boardOne.minions[1].isGold == False)
        assert(len([x for x in boardOne.minions if x.hasDivineShield]) == 0)
        assert(len([x for x in boardOne.minions if not x.hasDivineShield]) == 3)

        
        mockSource = MagicMock()
        mockSource.hasPoisonous = False
        testMinion.recieve_damage(1, mockSource)
        manager.check_for_death()
        manager.combat_substep()
        
        assert(len(boardOne.minions) == 2)
        assert(boardOne.minions[0].name == defaultMinion)
        assert(boardOne.minions[1].name == defaultMinion)
        
        assert(len([x for x in boardOne.minions if not x.hasDivineShield]) == 1)
        shielded = [x for x in boardOne.minions if x.hasDivineShield]
        assert(len(shielded) == 1)
        results.append((boardOne.minions.index(shielded[0])))
    assert(len(set(results)) > 1)
    assert(len(set(results)) != 100)

    
def test_gold_selfless_hero_dr():
    results = []
    for i in range(100):
        manager = GameManager(repo)
        manager.set_first_player(1)
        testMinion = manager.create_minion("Selfless Hero", isGold=True)
        
        manager.assign_minion_to_board(manager.create_minion(defaultMinion), 1)
        manager.assign_minion_to_board(testMinion, 1)
        manager.assign_minion_to_board(manager.create_minion(defaultMinion), 1)
        manager.assign_minion_to_board(manager.create_minion(defaultMinion), 1)

        boardOne = manager.get_player_board(1)
        assert(boardOne.minions[1] == testMinion)
        assert(boardOne.minions[1].isGold == True)
        assert(len([x for x in boardOne.minions if x.hasDivineShield]) == 0)
        assert(len([x for x in boardOne.minions if not x.hasDivineShield]) == 4)

        
        mockSource = MagicMock()
        mockSource.hasPoisonous = False
        testMinion.recieve_damage(2, mockSource)
        manager.check_for_death()
        manager.combat_substep()
        
        assert(len(boardOne.minions) == 3)
        assert(boardOne.minions[0].name == defaultMinion)
        assert(boardOne.minions[1].name == defaultMinion)
        assert(boardOne.minions[2].name == defaultMinion)

        
        assert(len([x for x in boardOne.minions if not x.hasDivineShield]) == 1)
        shielded = [x for x in boardOne.minions if x.hasDivineShield]
        assert(len(shielded) == 2)
        results.append((boardOne.minions.index(shielded[0]), boardOne.minions.index(shielded[0])))
    assert(len(set(results)) > 1)


def test_harvest_golem_dr():
    manager = GameManager(repo)
    manager.set_first_player(1)
    testMinion = manager.create_minion("Harvest Golem", isGold=False)
    
    manager.assign_minion_to_board(manager.create_minion(defaultMinion), 1)
    manager.assign_minion_to_board(testMinion, 1)
    manager.assign_minion_to_board(manager.create_minion(defaultMinion), 1)
    
    boardOne = manager.get_player_board(1)
    assert(boardOne.minions[1] == testMinion)
    assert(boardOne.minions[1].isGold == False)
    
    mockSource = MagicMock()
    mockSource.hasPoisonous = False
    testMinion.recieve_damage(3, mockSource)
    manager.check_for_death()
    manager.combat_substep()
    
    assert(len(boardOne.minions) == 3)
    assert(boardOne.minions[0].name == defaultMinion)
    assert(boardOne.minions[1].name == "Damaged Golem")
    assert(boardOne.minions[1].isGold == False)
    assert(boardOne.minions[1].currentHealth == 1)
    assert(boardOne.minions[1].attack == 2)
    assert(boardOne.minions[2].name == defaultMinion)
    

def test_gold_harvest_golem_dr():
    manager = GameManager(repo)
    manager.set_first_player(1)
    testMinion = manager.create_minion("Harvest Golem", isGold=True)
    
    manager.assign_minion_to_board(manager.create_minion(defaultMinion), 1)
    manager.assign_minion_to_board(testMinion, 1)
    manager.assign_minion_to_board(manager.create_minion(defaultMinion), 1)
    
    boardOne = manager.get_player_board(1)
    assert(boardOne.minions[1] == testMinion)
    assert(boardOne.minions[1].isGold == True)
    
    mockSource = MagicMock()
    mockSource.hasPoisonous = False
    testMinion.recieve_damage(6, mockSource)
    manager.check_for_death()
    manager.combat_substep()
    
    assert(len(boardOne.minions) == 3)
    assert(boardOne.minions[0].name == defaultMinion)
    assert(boardOne.minions[1].name == "Damaged Golem")
    assert(boardOne.minions[1].isGold == True)
    assert(boardOne.minions[1].currentHealth == 2)
    assert(boardOne.minions[1].attack == 4)
    assert(boardOne.minions[2].name == defaultMinion)
    
        
def test_kaboom_bot():
    results = []
    for i in range(100):
        manager = GameManager(repo)
        manager.set_first_player(1)
        testMinion = manager.create_minion("Kaboom Bot", isGold=False)
        
        manager.assign_minion_to_board(testMinion, 1)
        manager.assign_minion_to_board(manager.create_minion(highHealthMinion), 2)
        manager.assign_minion_to_board(manager.create_minion(highHealthMinion), 2)
        manager.assign_minion_to_board(manager.create_minion(highHealthMinion), 2)
        manager.assign_minion_to_board(manager.create_minion(highHealthMinion), 2)
        manager.assign_minion_to_board(manager.create_minion(highHealthMinion), 2)
        manager.assign_minion_to_board(manager.create_minion(highHealthMinion), 2)
        manager.assign_minion_to_board(manager.create_minion(highHealthMinion), 2)

        boardOne = manager.get_player_board(1)
        boardTwo = manager.get_player_board(2)
        assert(boardOne.minions[0] == testMinion)
        assert(boardOne.minions[0].isGold == False)
        
        mockSource = MagicMock()
        mockSource.hasPoisonous = False
        testMinion.recieve_damage(2, mockSource)
        manager.check_for_death()
        manager.combat_substep()
        
        assert(len(boardOne.minions) == 0)
        assert(len(boardTwo.minions) == 7)
        assert(len([x for x in boardTwo.minions if x.currentHealth == x.maxHealth]) == 6)
        damagedMinions = list(filter(lambda x: x.currentHealth == 1, boardTwo.minions))
        assert(len(damagedMinions) == 1)
        results.append((boardTwo.minions.index(damagedMinions[0])))
    assert(len(set(results)) > 1)


def test_gold_kaboom_bot():
    results = []
    for i in range(100):
        manager = GameManager(repo)
        manager.set_first_player(1)
        testMinion = manager.create_minion("Kaboom Bot", isGold=True)
        
        manager.assign_minion_to_board(testMinion, 1)
        manager.assign_minion_to_board(manager.create_minion(highHealthMinion), 2)
        manager.assign_minion_to_board(manager.create_minion(highHealthMinion), 2)
        manager.assign_minion_to_board(manager.create_minion(highHealthMinion), 2)
        manager.assign_minion_to_board(manager.create_minion(highHealthMinion), 2)
        manager.assign_minion_to_board(manager.create_minion(highHealthMinion), 2)
        manager.assign_minion_to_board(manager.create_minion(highHealthMinion), 2)
        manager.assign_minion_to_board(manager.create_minion(highHealthMinion), 2)

        boardOne = manager.get_player_board(1)
        boardTwo = manager.get_player_board(2)
        assert(boardOne.minions[0] == testMinion)
        assert(boardOne.minions[0].isGold == True)
        
        mockSource = MagicMock()
        mockSource.hasPoisonous = False
        testMinion.recieve_damage(4, mockSource)
        manager.check_for_death()
        manager.combat_substep()
        
        assert(len(boardOne.minions) == 0)
        assert(len(boardTwo.minions) == 7)
        assert(len([x for x in boardTwo.minions if x.currentHealth == x.maxHealth]) == 5)
        damagedMinions = list(filter(lambda x: x.currentHealth == 1, boardTwo.minions))
        assert(len(damagedMinions) == 2)
        results.append((boardTwo.minions.index(damagedMinions[0]), (boardTwo.minions.index(damagedMinions[1]))))
    assert(len(set(results)) > 1)
        
        
def test_gold_mounted_raptor_def():
    results = []
    for i in range(100):
        manager = GameManager(repo)
        manager.set_first_player(1)
        testMinion = manager.create_minion("Mounted Raptor", isGold=True)
        
        manager.assign_minion_to_board(manager.create_minion(highHealthMinion), 1)  # Uses highHealthMinion as default minion is 1-cost
        manager.assign_minion_to_board(testMinion, 1)
        manager.assign_minion_to_board(manager.create_minion(highHealthMinion), 1)
        
        boardOne = manager.get_player_board(1)
        assert(boardOne.minions[1] == testMinion)
        assert(boardOne.minions[1].isGold == True)
        
        mockSource = MagicMock()
        mockSource.hasPoisonous = False
        testMinion.recieve_damage(99, mockSource)
        manager.check_for_death()
        manager.combat_substep()
        
        assert(len(boardOne.minions) == 4)
        assert(boardOne.minions[0].name == highHealthMinion)
        assert(boardOne.minions[1].name not in [highHealthMinion, "Mounted Raptor"])
        assert(boardOne.minions[1].isGold == True)
        assert(boardOne.minions[1].cost == 1)
        assert(boardOne.minions[2].name not in [highHealthMinion, "Mounted Raptor"])
        assert(boardOne.minions[2].isGold == True)
        assert(boardOne.minions[2].cost == 1)
        assert(boardOne.minions[3].name == highHealthMinion)
        results.append((boardOne.minions[1].name, boardOne.minions[2].name))
    assert(len(set(results)) > 1)
    
            
        
        
        
        
        
        
        
        
        
        
