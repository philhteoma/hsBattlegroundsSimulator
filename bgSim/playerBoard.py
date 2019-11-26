from bgSim.minionBoard import MinionBoard

class PlayerBoard:
    def __init__(self, boardNumber):
        self.boardNumber = boardNumber
        self.minions = MinionBoard(self)
        self.deathrattles = []
        self.staticEffects = []
        self.personalEffects = []
        
        self.deadMinions = []
        self.usedMinions = []
        self.activeMinionIndex = 0
    
    def add_minion_to_right(self, minion):
        """
            Adds a minion to the rightmost position of the board
        """
        return self.minions.add_minion_to_right(minion)
    
    
    def add_minion_at_index(self, minion, index):
        """
            Adds a minion at position "index" of the board
        """
        return self.minion.add_minion_at_index(self, minion, index)
    
    
    def add_minion_with_reference(self, newMinion, referenceMinion):
        """
            Adds a minion to the right of the reference minion
            If said minion is no longer on the board, adds it to the right of its previous left neighbour, or that minions children
            If no left neighbours remain, adds minion at index 0
        """
        self.minions.add_minion_with_reference(newMinion, referenceMinion)
        
    
    def remove_minion(self, minion):
        self.minions.remove(minion)
    
    
    def remmove_minion_by_index(self, index):
        self.minions.pop(index)
    
    
    def update_minion_data(self):
        self._update_minion_locations()
        self._update_static_effects()
        self._update_personal_effects()
        self._update_deathrattles()
        self._reset_anthems()
        self._update_minion_stats()
        self._update_for_lethal_damage()

    
    
    def get_leftmost_minion(self):
        return self.minions[0]
    
    
    def get_attackable_targets(self):
        taunts = [x for x in self.minions if x.hasTaunt == True]
        if len(taunts) > 0:
            return taunts
        else:
            return self.minions
    
    
    def apply_buff(self, minion, buff):
        minion.buffs.append(buff)

    
    
    def _update_for_lethal_damage(self):
        for minion in self.minions:
            if minion.currentHealth <= 0:
                minion.isDead = True
    
    def _update_minion_locations(self):
        for minion in self.minions:
            minion.location = self.minions.index(minion)
    
    
    def _update_static_effects(self):
        """
            Denesting list comprehension in the form [x for y in z for x in y]
            Unpacks all minions static effects into one flat list
            Method uses minion order left to right, preserves effect order in minions themselves
        """
        self.staticEffects = [effect for minion in self.minions for effect in minion.staticEffects]
    
    
    def _update_personal_effects(self):
        """
            Denesting list comprehension in the form [x for y in z for x in y]
            Unpacks all minions personal effects into one flat list
            Method uses minion order left to right, preserves effect order in minions themselves
        """
        self.personalEffects = [effect for minion in self.minions for effect in minion.personalEffects]
        
    def _update_deathrattles(self):
        """
            Denesting list comprehension in the form [x for y in z for x in y]
            Unpacks all minions deathrattles into one flat list
            Method uses minion order left to right, preserves effect order in minions themselves
        """
        self.deathrattles = [dr for minion in self.minions for dr in minion.deathrattles]
    
    
    def _reset_anthems(self):
        for minion in self.minions:
            minion.buffs = [x for x in minion.buffs if x.buffType != "anthem"]
        
        anthems = [x for x in self.staticEffects if x.effectType == "anthem"]
        for anthem in anthems:
            for minion in self.minions:
                if anthem.condition(minion):
                    self.apply_buff(minion, anthem.get_buff())
    
    
    def _update_minion_stats(self):
        for minion in self.minions:
            minion.update_stats()
    
