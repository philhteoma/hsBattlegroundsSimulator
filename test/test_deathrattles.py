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
    
    board = MagicMock()
    attrs = {"get_player_board.return_value" : board}
    manager.configure_mock(**attrs)
    
    rattle = dr.MecharooDr(minion)
    rattle.run(manager)
    
    manager.get_player_board.assert_called()
    manager.create_minion.assert_called()
    board.add_minion_with_reference.assert_called()
    

def  test_SelflessHeroDr():
    minion = MagicMock()
    manager = MagicMock()
    
    rattle = dr.SelflessHeroDr(minion)
    rattle.run(manager)
    
    manager.get_player_board.assert_called()
