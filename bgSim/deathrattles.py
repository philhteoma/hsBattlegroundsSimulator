import random
from bgSim.gameEvents import SummonEvent


class Deathrattle:
    pass


class SummonDeathrattle(Deathrattle):
    def summon_minion(self, newMinion, manager):
        ownerBoard = manager.get_player_board(self.minion.boardNumber)
        ownerBoard.add_minion_with_reference(newMinion, self.minion)
        print("{} summons a {}".format(self.minion.name, newMinion.name))


class SummonOpponentDeathrattle(Deathrattle):
    pass


class BuffDeathrattle(Deathrattle):
    pass


class AttackDeathrattle(Deathrattle):
    pass


class OtherDeathrattle(Deathrattle):
    pass

 
class MecharooDr(SummonDeathrattle):
    name = "mecharoo_dr"
    text = "Summon a 1/1 Jo-E Bot."
    
    def __init__(self, minion):
        self.minionId = minion.id
        self.minion = minion

    
    def run(self, manager):
        isGold = self.minion.isGolden
        minionToSpawn = manager.create_minion("Jo-E Bot", isGold)
        super().summon_minion(minionToSpawn, manager)


class SelflessHeroDr(BuffDeathrattle):
    name = "selfess_hero_dr"
    text = "Give a random friendly minion Divine Shield."
    
    
    def __init__(self, minion):
        self.minionId = minion
        self.minion = minion
    
    
    def run(self, manager):
        owner = self.minion.boardNumber
        targets = manager.get_player_board(owner).minions
        if len(targets) > 0:
            target  = random.choice(targets)
            target.hasDivineShield = True
        else:
            pass



classList = [
    MecharooDr,
    SelflessHeroDr,
    ]

deathrattles = {x.name: x for x in classList}


def get_deathrattle(name):
    return deathrattles[name]
    
