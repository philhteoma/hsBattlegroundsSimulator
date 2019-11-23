from bgSim.minionBoard import MinionBoard
from unittest.mock import MagicMock

def test_set_next_active_minion_simple():
    masterBoard = MagicMock()
    minionBoard = MinionBoard(masterBoard)
    
    minionA = MagicMock()
    minionA.name = "MinionA"
    
    minionB = MagicMock()
    minionB.name = "MinionB"
    
    minionBoard.minions = [minionA, minionB]
    
    minionBoard.set_next_active_minion()
    
    assert(minionBoard.activeMinion == minionA)
    assert(minionBoard.boardSnapshot == [minionA, minionB])
    

def test_set_next_active_minion_midway():
    masterBoard = MagicMock()
    minionBoard = MinionBoard(masterBoard)
    
    minionA = MagicMock()
    minionB = MagicMock()
    minionC = MagicMock()
    minionD = MagicMock()
    
    minionBoard.minions = [minionA, minionB, minionC, minionD]
    minionBoard.boardSnapshot = [minionA, minionB, minionC, minionD]
    minionBoard.activeMinion = minionB
    
    minionBoard.set_next_active_minion()
    
    assert(minionBoard.activeMinion == minionC)
    assert(minionBoard.boardSnapshot == [minionA, minionB, minionC, minionD])
    
    
def test_set_next_active_minion_active_minion_dead():
    masterBoard = MagicMock()
    minionBoard = MinionBoard(masterBoard)
    
    minionA = MagicMock()
    minionB = MagicMock()
    minionC = MagicMock()
    minionD = MagicMock()

    minionBoard.minions = [minionA, minionC, minionD]
    minionBoard.boardSnapshot = [minionA, minionB, minionC, minionD]
    minionBoard.activeMinion = minionB
    
    minionBoard.set_next_active_minion()
    
    assert(minionBoard.activeMinion == minionC)
    assert(minionBoard.boardSnapshot == [minionA, minionC, minionD])
    
    
def test_set_next_active_minion_active_children():
    masterBoard = MagicMock()
    minionBoard = MinionBoard(masterBoard)
    
    minionA = MagicMock()
    minionB = MagicMock()
    minionC = MagicMock()
    minionD = MagicMock()
    
    childB1 = MagicMock()
    childB1.parentMinions = [minionB]
    
    minionBoard.minions = [minionA, childB1, minionC, minionD]
    minionBoard.boardSnapshot = [minionA, minionB, minionC, minionD]
    minionBoard.activeMinion = minionB
    
    minionBoard.set_next_active_minion()
    
    assert(minionBoard.activeMinion == childB1)
    assert(minionBoard.boardSnapshot == [minionA, childB1, minionC, minionD])


def test_set_next_active_minion_multiple_active_children():
    masterBoard = MagicMock()
    minionBoard = MinionBoard(masterBoard)
    
    minionA = MagicMock()
    minionB = MagicMock()
    minionC = MagicMock()
    minionD = MagicMock()
    
    childB1 = MagicMock()
    childB2 = MagicMock()
    childB3 = MagicMock()
    
    childB1.parentMinions = [minionB]
    childB2.parentMinions = [minionB]
    childB3.parentMinions = [minionB]
    
    minionBoard.minions = [minionA, childB1, childB2, childB3, minionC, minionD]
    minionBoard.boardSnapshot = [minionA, minionB, minionC, minionD]
    minionBoard.activeMinion = minionB
    
    minionBoard.set_next_active_minion()
    
    assert(minionBoard.activeMinion == childB1)
    assert(minionBoard.boardSnapshot == [minionA, childB1, childB2, childB3, minionC, minionD])


def test_set_next_active_minion_right_minions_children():
    masterBoard = MagicMock()
    minionBoard = MinionBoard(masterBoard)
    
    minionA = MagicMock()
    minionB = MagicMock()
    minionC = MagicMock()
    minionD = MagicMock()
    
    childC1 = MagicMock()
    childC2 = MagicMock()
    childC3 = MagicMock()
    
    childC1.parentMinions = [minionC]
    childC2.parentMinions = [minionC]
    childC3.parentMinions = [minionC]
    
    minionBoard.minions = [minionA, childC1, childC2, childC3, minionD]
    minionBoard.boardSnapshot = [minionA, minionB, minionC, minionD]
    minionBoard.activeMinion = minionB
    
    minionBoard.set_next_active_minion()
    
    assert(minionBoard.activeMinion == childC1)
    assert(minionBoard.boardSnapshot == [minionA, childC1, childC2, childC3, minionD])


def test_set_next_active_minion_all_children():
    masterBoard = MagicMock()
    minionBoard = MinionBoard(masterBoard)
    
    minionA = MagicMock()
    minionB = MagicMock()
    minionC = MagicMock()
    minionD = MagicMock()
    
    childA1 = MagicMock()
    childB1 = MagicMock()
    childC1 = MagicMock()
    
    childA1.parentMinions = [minionA]
    childB1.parentMinions = [minionB]
    childC1.parentMinions = [minionC]
    
    minionBoard.minions = [childA1, childB1, childC1]
    minionBoard.boardSnapshot = [minionA, minionB, minionC, minionD]
    minionBoard.activeMinion = minionB
    
    minionBoard.set_next_active_minion()
    
    assert(minionBoard.activeMinion == childB1)
    assert(minionBoard.boardSnapshot == [childA1, childB1, childC1])
    

def test_set_next_active_minion_active_children_parent_lives():
    masterBoard = MagicMock()
    minionBoard = MinionBoard(masterBoard)
    
    minionA = MagicMock()
    minionB = MagicMock()
    minionC = MagicMock()
    minionD = MagicMock()
    
    childB1 = MagicMock()
    
    childB1.parentMinions = [minionB]
    
    minionBoard.minions = [minionA, minionB, childB1, minionC, minionD]
    minionBoard.boardSnapshot = [minionA, minionB, minionC, minionD]
    minionBoard.activeMinion = minionB
    
    minionBoard.set_next_active_minion()
    
    assert(minionBoard.activeMinion == childB1)
    assert(minionBoard.boardSnapshot ==  [minionA, minionB, childB1, minionC, minionD])
    

def test_set_next_active_minion_right_minions_children_parent_lives():
    masterBoard = MagicMock()
    minionBoard = MinionBoard(masterBoard)
    
    minionA = MagicMock()
    minionB = MagicMock()
    minionC = MagicMock()
    minionD = MagicMock()
    
    childC1 = MagicMock()
    
    childC1.parentMinions = [minionC]
    
    minionBoard.minions = [minionA, minionC, childC1, minionD]
    minionBoard.boardSnapshot = [minionA, minionB, minionC, minionD]
    minionBoard.activeMinion = minionB
    
    minionBoard.set_next_active_minion()
    
    assert(minionBoard.activeMinion == minionC)
    assert(minionBoard.boardSnapshot ==  [minionA, minionC, childC1, minionD])


def test_set_next_active_minion_loop():
    masterBoard = MagicMock()
    minionBoard = MinionBoard(masterBoard)
    
    minionA = MagicMock()
    minionB = MagicMock()
    minionC = MagicMock()
    minionD = MagicMock()
    
    minionBoard.minions = [minionA, minionB, minionC, minionD]
    minionBoard.boardSnapshot = [minionA, minionB, minionC, minionD]
    minionBoard.activeMinion = minionD
    
    minionBoard.set_next_active_minion()
    
    assert(minionBoard.activeMinion == minionA)
    assert(minionBoard.boardSnapshot == [minionA, minionB, minionC, minionD])


def test_add_minion_with_reference():
    masterBoard = MagicMock()
    minionBoard = MinionBoard(masterBoard)
    
    minionA = MagicMock()
    minionB = MagicMock()
    minionC = MagicMock()
    
    newMinion = MagicMock()
    
    minionBoard.minions = [minionA, minionB, minionC]
    minionBoard.add_minion_with_reference(newMinion, minionB)
    
    assert(minionBoard.minions == [minionA, minionB, newMinion, minionC])


def test_add_minion_with_reference_dead_minion():
    masterBoard = MagicMock()
    minionBoard = MinionBoard(masterBoard)
    
    minionA = MagicMock()
    minionB = MagicMock()
    minionC = MagicMock()
    
    newMinion = MagicMock()
    
    minionBoard.minions = [minionA, minionC]
    minionBoard.boardSnapshot = [minionA, minionB, minionC]
    minionBoard.add_minion_with_reference(newMinion, minionB)
    
    assert(minionBoard.minions == [minionA, newMinion, minionC])
    

def test_add_minion_with_reference_dead_minion_and_child_neighbour():
    masterBoard = MagicMock()
    minionBoard = MinionBoard(masterBoard)
    
    minionA = MagicMock()
    minionB = MagicMock()
    minionC = MagicMock()
    
    childA1 = MagicMock()
    childA2 = MagicMock()
    childA1.parentMinions = [minionA]
    childA2.parentMinions = [minionA]
    
    newMinion = MagicMock()
    
    minionBoard.minions = [childA1, childA2, minionC]
    minionBoard.boardSnapshot = [minionA, minionB, minionC]
    minionBoard.add_minion_with_reference(newMinion, minionB)
    
    assert(minionBoard.minions == [childA1, childA2, newMinion, minionC])


def test_add_minion_with_reference_all_left_minions_dead():
    masterBoard = MagicMock()
    minionBoard = MinionBoard(masterBoard)
    
    minionA = MagicMock()
    minionB = MagicMock()
    minionC = MagicMock()
    
    newMinion = MagicMock()
    
    minionBoard.minions = [minionC]
    minionBoard.boardSnapshot = [minionA, minionB, minionC]
    minionBoard.add_minion_with_reference(newMinion, minionB)
    
    assert(minionBoard.minions == [newMinion, minionC])


def test_get_active_minion():
    masterBoard = MagicMock()
    minionBoard = MinionBoard(masterBoard)
    
    minionA = MagicMock()
    
    minionBoard.activeMinion = minionA
    
    assert(minionBoard.get_active_minion() == minionA)


def test_add_minion_to_right():
    masterBoard = MagicMock()
    minionBoard = MinionBoard(masterBoard)
    
    minionA = MagicMock()
    minionB = MagicMock()
    minionC = MagicMock()
    
    minionBoard.minions = [minionA, minionB]
    minionBoard.add_minion_to_right(minionC)
    
    assert(minionBoard.minions == [minionA, minionB, minionC])


def test_add_minion_to_right_empty_minion_list():
    masterBoard = MagicMock()
    minionBoard = MinionBoard(masterBoard)
    
    minionA = MagicMock()
    
    minionBoard.minions = []
    minionBoard.add_minion_to_right(minionA)
    
    assert(minionBoard.minions == [minionA])

    
    
    
    
