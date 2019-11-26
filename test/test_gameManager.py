from bgSim.gameManager import GameManager
from unittest.mock import MagicMock

class repoRepo:
    """
        Quick setup to allow a mock minion repo to generate minions with sequentially increasing ids
    """
    def __init__(self):
        self.idCount = 1
        
    
    def create_minion(self):
        minion = MagicMock()
        minion.id = self.idCount
        self.idCount += 1
        return minion
    
    
    def get_test_minion_repo(self):
        repo = MagicMock()
        repo.configure_mock(**{"create_minion.return_value" : self.create_minion()})
        return repo


repoRepo = repoRepo()


def test_init():
    repo = repoRepo.get_test_minion_repo()
    manager = GameManager(repo)
    
    assert(len(manager._boards.keys()) == 2)


def test_create_minion():
    repo = repoRepo.get_test_minion_repo()
    manager = GameManager(repo)
    
    minion = manager.create_minion("Test")
    
    repo.create_minion.assert_called()
    
