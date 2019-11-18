from playerBoard import PlayerBoard
from minionRepository import MinionRepository
from combatEvents import get_combat_event
import random

class GameManager:
    def __init__(self, minionRepo):
        minionRepo = MinionRepository(csvPath = minionRepo)
        
        boardOne = PlayerBoard(1)
        boardTwo = PlayerBoard(2)
        
        _boards = {
            1 : self.boardOne
            2 : self.boardTwo
            }
        
        combatStack = []
    
    
    def create_minion(self, minionName, isGolden=False):
        return minionRepo.create_minion(minionName)
    
    
    def assign_minion_to_board(self, minion, boardNumber, index=-1):
        if index == -1:
            self._boards[boardNumber].add_minion_to_right(minion)
        else:
            self._boards[boardNumber].add_minion_at_index(minion, index)
    
    
    def flip_active_player(self):
        if self.activePlayer == 2:
            self.activePlayer = 1
        else:
            self.activePlayer = 2
    
    
    def get_active_board(self):
        return self._boards[self.activePlayer]
    
    
    def get_inactive_board(self):
        inactivePlayer = 1 if self.activePlayer == 2 else 2
        return self._boards[inactivePlayer]
    
    
    def set_first_player(self, firstPlayer):
        """
            Sets first player if specified, otherwise chooses randomly
        """
        if not firstPlayer:
            firstPlayer = random.choice(_board.keys()])
        self.activePlayer = firstPlayer
    
    
    def run_full_combat(self, firstPlayer=None):
        # Main Combat Loop
        while len(boardOne.minions) > 0 and len(boardTwo.minions) > 0:
            self.combat_step()
            
        
    def refresh_player_boards(self):
        self.boardOne.update_minion_data()
        self.boardTwo.update_minion_data()
        
        
    def combat_step():
        self.flip_active_player()
        starterEvent = get_combat_event("choose_attack_target")
        activeEvent = starterEvent(self)
        self.combatStack.append(activeEvent)
        
        while len(self.combatStack) > 0:
            self.combatSubstep()
    
    
    def combat_substep(self):
        activeEvent = self.combatStack.pop(0)
        activeEvent.run()
        self.refresh_player_boards()
        self.check_for_death()
            
                    
                
    
