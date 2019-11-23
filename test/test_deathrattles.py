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
    minion = MagicMock()
    manager = MagicMock()
    
    rattle = dr.MecharooDr(minion)
    rattle.run(mockManager)
    
    manager.create_minion.assert_called()
    
    


def  test_SelflessHeroDr():
    minion = MagicMock()
    manager = MagicMock()
    
    rattle = dr.SelflessHeroDr(minion)
    rattle.run(manager)
