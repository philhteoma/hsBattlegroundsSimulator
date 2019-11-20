from constants import MAX_MINION_COUNT

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
        
    
    def remove_minion(self, minion):
        self.minions.remove(minion)
    
    
    def remmove_minion_by_index(self, index):
        self.minions.pop(index)
    
    
    def update_minion_data(self):
        self._update_for_lethal_damage()
        self._update_minion_locations()
        self._update_static_effects()
        self._update_personal_effects()
        self._update_deathrattles()
    
    
    def get_leftmost_minion(self):
        return self.minions[0]
    
    
    def get_attackable_targets(self):
        taunts = [x for x in self.minions if x.hasTaunt == True]
        if len(taunts) > 0:
            return taunts
        else:
            return self.minions
    
    
    def _update_for_lethal_damage(self):
        for minion in self.minions:
            if minion.health <= 0:
                minion.isDead = True
    
    def _update_minion_locations(self):
        for minion in self.minions:
            minion.position = self.minions.index(minion)
    
    
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
        


class MinionBoard():
    def __init__(self, masterBoard):
        self.masterBoard = masterBoard
        self.activeMinion = None
        self.theoretialAttackOrder = []
        self.activeMinionIndex = 0
        self.minions = []
        
    
    def set_next_active_minion(self):
        nextActiveMinion = None
        if childMinions := self.check_for_child_minions(self.activeMinion): # := := := I AM THE WALRUS := := :=
            nextActiveMinion = childMinions[0]
        else:
            for minion in self.theoretialAttackOrder:
                if minion in self.minions:
                    nextActiveMinion = minion
                    break
                elif childMinions := self.check_for_child_minions(minion):
                    for cMinion in childMinions:
                        if cMinion in self.minions:
                            nextActiveMinion = cMinion
                            break
                    if nextActiveMinion:
                        break
        
        if not nextActiveMinion:
            nextActiveMinion = self.minions[0]
        
        self.activeMinion = nextActiveMinion
        self.activeMinionIndex = self.minions.index(self.activeMinion)
        self.theoreticalAttackOrder = self.minion[self.activeMinionIndex+1:]
            
    
    def get_active_minion(self):
        return self.activeMinion
    
    
    def check_for_child_minions(self, minion):
        """
            Scans for minions which spawned from the given minion instance
        """
        return list(filter(lambda x: minion in x.parentMinions, self.minions))
    
    
    def add_minion_to_right(self, minion):
        self.theoretialAttackOrder.append(minion) # Hello Finkle Einhorn. Here's the bit which means you won't miss your attack.
        minion.set_board_number(self.masterBoard.boardNumber)
        self.add_minion_at_index(minion, len(self.minions))
        
        
    def add_minion_at_index(self, minion, index):
        if len(self.minions) > MAX_MINION_COUNT:
            return False
        else:
            self.minions.insert(index, minion)
            minion.set_board_number(self.masterBoard.boardNumber)
            self.masterBoard.update_minion_data()
            return True
    

    def __getitem__(self, index):
        """
            Allows the class instance to behave like a list for purposes of iterating, getting items, slicing and similar
            More info at https://stackoverflow.com/questions/36688966/let-a-class-behave-like-its-a-list-in-python
        """
        return self.minions[index]
    
    
    def __len__(self):
        return len(self.minions)
    
    
    def index(self, index):
        return self.minions.index(index)
    
    
    def remove(self, item):
        self.minions.remove(item)
    

    def print_why_minion_attack_order_is_hell(self):
        damnedLogic = """
            So minion attack order works like this
            Minions attack from left to right. Nice and easy.
            However, this is complicated by minions that spawn other minions, typically on taking damage, or death.
            If minions get spawn to the left of the minion that last attacked, those minions don't get to attack until the attack order wheels back round to them.
            Minions spawned to the right will get to attack in order.
            Both these things makes sense.
            However, if the last minion to attack dies and spawns minions, those minions will attack next.
            """
        
        
        
