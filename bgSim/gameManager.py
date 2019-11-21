from bgSim.playerBoard import PlayerBoard
from bgSim.minionRepository import MinionRepository
from bgSim.combatEvents import get_combat_event
import random

class GameManager:
    def __init__(self, minionRepo):
        
        if "create_minion" not in dir(minionRepo):
            raise ValueError("minionRepo must have a create_minion method")

        self.minionRepo = minionRepo
                        
        self.boardOne = PlayerBoard(1)
        self.boardTwo = PlayerBoard(2)
        
        self._boards = {
            1 : self.boardOne,
            2 : self.boardTwo,
            }
        
        self.combatStack = []
        
        self.activeMinion = {
            1 : None,
            2:  None,
            }
    
    
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
    
    
    def get_player_board(self, playerNumber):
        return self._boards[playerNumber]
    
    
    def get_active_board(self):
        return self._boards[self.activePlayer]
    
    
    def get_inactive_board(self):
        inactivePlayer = 1 if self.activePlayer == 2 else 2
        return self._boards[inactivePlayer]
    
    
    def set_next_active_minion(self):
        return self.minions.set_next_active_minion()
    
    
    def set_first_player(self, firstPlayer=None):
        """
            Sets first player if specified, otherwise chooses randomly
        """
        if not firstPlayer:
            firstPlayer = random.choice(list(self._boards.keys()))
        self.activePlayer = firstPlayer
    
    
    def check_for_death(self):
        activeDead = list(filter(lambda x: x.isDead, self.get_active_board().minions))
        activeDeathrattles = [x for y in activeDead for x in y.deathrattles]
        
        inactiveDead = list(filter(lambda x: x.isDead, self.get_inactive_board().minions))
        inactiveDeathrattles = [x for y in inactiveDead for x in y.deathrattles]
        
        self.combatStack = activeDeathrattles + inactiveDeathrattles + self.combatStack
        
        for minion in activeDead:
            self.get_active_board().remove_minion(minion)
        
        for minion in inactiveDead:
            self.get_inactive_board().remove_minion(minion)
                
    
    def run_full_combat(self, firstPlayer=None):
        # Main Combat Loop
        while len(self.boardOne.minions) > 0 and len(self.boardTwo.minions) > 0:
            self.combat_step()
            
        
    def refresh_player_boards(self):
        self.boardOne.update_minion_data()
        self.boardTwo.update_minion_data()
        
        
    def combat_step(self):
        self.flip_active_player()
        starterEvent = get_combat_event("choose_attack_target")
        activeEvent = starterEvent()
        self.combatStack.append(activeEvent)
        
        # Run combat event, then run events until the stack is empty
        # Then check for death and add any new combat events. Then run until the stack is empty.
        # Repeat untul the stack is empty after checking for minion death.
        while len(self.combatStack) > 0:
            while len(self.combatStack) > 0:
                self.combat_substep()
            self.check_for_death()
    
    
    def combat_substep(self):
        activeEvent = self.combatStack.pop(0)
        activeEvent.run(self)
        self.refresh_player_boards()
        if len(self.combatStack) > 0:
            self.combat_substep()
            
                    
                
    
