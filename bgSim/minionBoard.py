from bgSim.constants import MAX_MINION_COUNT

class MinionBoard():
    def __init__(self, masterBoard):
        self.masterBoard = masterBoard
        self.activeMinion = None
        
        self.minions = []
        self.boardSnapshot = []

    
    def set_next_active_minion(self):
        nextActiveMinion = None

        if not self.activeMinion:
            nextActiveMinion = self.minions[0]
        elif childMinions := self._check_for_child_minions(self.activeMinion, self.minions): # := := := I AM THE WALRUS := := :=
            nextActiveMinion = childMinions[0]
        else:
            theoretialAttackOrder = self._get_theoretical_attack_order(self.activeMinion)
            for minion in theoretialAttackOrder:
                if minion in self.minions:
                    nextActiveMinion = minion
                    break
                elif childMinions := self._check_for_child_minions(minion, self.minions):
                    for cMinion in childMinions:
                        if cMinion in self.minions:
                            nextActiveMinion = cMinion
                            break
                    if nextActiveMinion:
                        break
        
        if not nextActiveMinion:
            nextActiveMinion = self.minions[0]
        
        self.activeMinion = nextActiveMinion
        self.boardSnapshot = self.minions.copy()
            
    
    def _get_theoretical_attack_order(self, minionReference):
        """
            Returns a slice of self.boardSnapshot which includes every minion to the right of the provided minion
        """
        minionIndex = self.boardSnapshot.index(minionReference)
        return self.boardSnapshot[minionIndex+1:]
    
    
    def add_minion_with_reference(self, newMinion, referenceMinion):
        if referenceMinion in self.minions:
            self.add_minion_at_index(newMinion, self.minions.index(referenceMinion) + 1) # +1 adds minion to right of its parent
        else:
            if leftNeighbour := self._get_minions_left_neighbour(referenceMinion):
                self.add_minion_at_index(newMinion, self.minions.index(leftNeighbour) + 1)
            else:
                self.add_minion_at_index(newMinion, 0) # Adds to leftmost position if no neighbours can be found
        
        print([x.name for x in self.minions])

    
    def _get_minions_left_neighbour(self, minion):
        """
            Uses the board snapshot to return the minion that is now directly to the left of the given minion
            Uses the boardSnapshot rather than the actual board to allow functioning even if the minion is dead
            Returns None if no suitable minions are found - simply means minion will be added to the leftmost position of the board
        """
        index = self.boardSnapshot.index(minion)
        minionsToLeft = self.boardSnapshot[:index]
        
        targetMinion = None
        # Move backwards through list to find nearest living relative
        for referenceMinion in minionsToLeft[::-1]:  #[::-1] Reverses the list its applied to
            if referenceMinion in self.minions:
                targetMinion = referenceMinion
                break
            elif childMinions := self._check_for_child_minions(referenceMinion, self.minions):
                targetMinion = childMinions[-1]
                break
        
        return targetMinion
        
    
    def get_active_minion(self):
        return self.activeMinion
    
    
    def _check_for_child_minions(self, minion, minionList):
        """
            Scans for minions which spawned from the given minion instance
        """
        return list(filter(lambda x: minion in x.parentMinions, self.minions))
    
    
    def add_minion_to_right(self, minion):
        self.boardSnapshot.append(minion) # Hello Finkle Einhorn. Here's the bit which means you won't miss your attack.
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
            The test file for this class is currently 334 lines long, mostly because of this nonsense
            """
        
        print(damnedLogic)
        
        
        
