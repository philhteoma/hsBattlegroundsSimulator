# Unit tests for Deathrattles

from unittest.mock import MagicMock
import bgSim.deathrattles as dr


def  test_Deathrattle():
    pass


def  test_SummonDeathrattle():
    pass


def  test_SummonOpponentDeathrattle():
    pass


def  test_BuffDeathrattle():
    pass


def  test_AttackDeathrattle():
    pass


def  test_OtherDeathrattle():
    pass

 
def  test_MecharooDr():
    mockMinion = MagicMock()
    mockManager = MagicMock()
    
    rattle = dr.MecharooDr(mockMinion)
    rattle.run(mockManager)
    


def  test_SelflessHeroDr():
    mockMinion = MagicMock()
    mockManager = MagicMock()
    
    rattle = dr.SelflessHeroDr(mockMinion)
    rattle.run(mockManager)
