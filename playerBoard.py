from constants import MAX_MINION_COUNT

class PlayerBoard:
    def __init__(self, boardNumber):
        self.boardNumber = boardNumber
        self.minions = []
        self.deathrattles = []
        self.staticEffects = []
        self.personalEffects = []
        
        self.deadMinions = []
        
    
    def add_minion_to_right(self, minion):
        """
            Adds a minion to the rightmost position of the board
        """
        return self.add_minion_at_index(minion, len(self.minions),)
    
    
    def add_minion_at_index(self, minion, index):
        """
            Adds a minion at position "index" of the board
        """
        if len(self.minions) > MAX_MINION_COUNT:
            return False
        else:
            self.minions.insert(index, minion)
            minion.set_board_number(self.boardNumber)
            self.update_minion_data()
            return True
    
    def update_minion_data(self):
        self._update_minion_locations()
        self._update_static_effects()
        self._update_personal_effects()
        self._update_deathrattles()
    
    def get_leftmost_minion(self):
        return self.minions[0]
    
    
    def get_attackable_targets(self):
        taunts = [x for x in self.minions if x.hasTaunt == True]
        if len(taunts) > 1:
            return taunts
        else:
            return self.minions
    
    
    def _update_minion_locations(self):
        for minion in self.minions:
            minion.position = self.minions.index(minion)
    
    
    def _update_static_effects(self):
        """
            Unpacks all minions static effects into one flat list
            Method uses minion order left to right, preserves effect order in minions themselves
        """
        self.staticEffects = [effect for minion in self.minions for effect in minion.staticEffects]
    
    
    def _update_personal_effects(self):
        """
            Unpacks all minions personal effects into one flat list
            Method uses minion order left to right, preserves effect order in minions themselves
        """
        self.personalEffects = [effect for minion in self.minions for effect in minion.personalEffects]

        
    def _update_deathrattles(self):
        self.deathrattles = [dr for minion in self.minions for dr in minion.deathrattles]
        
