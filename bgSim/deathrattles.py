import random
from bgSim.gameEvents import SummonEvent
from bgSim.buffs import AttackBuff, HealthBuff

class Deathrattle:
    def __init__(self, minion):
        self.minion = minion
        self.minionId = minion.id


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
        super().__init__(minion)

    
    def run(self, manager):
        minionToSpawn = manager.create_minion("Jo-E Bot", isGold=False)
        super().summon_minion(minionToSpawn, manager)


class MecharooDrGold(SummonDeathrattle):
    name = "mecharoo_dr_gold"
    text = "Summon a 2/2 Jo-E Bot."
    def __init__(self, minion):
        super().__init__(minion)

    
    def run(self, manager):
        minionToSpawn = manager.create_minion("Jo-E Bot", isGold=True)
        super().summon_minion(minionToSpawn, manager)


class SelflessHeroDr(BuffDeathrattle):
    name = "selfess_hero_dr"
    text = "Give a random friendly minion Divine Shield."
    
    
    def __init__(self, minion):
        super().__init__(minion)
    
    
    def run(self, manager):
        owner = self.minion.boardNumber
        targets = manager.get_player_board(owner).minions
        if len(targets) > 0:
            target  = random.choice(targets)
            target.hasDivineShield = True
        else:
            pass
    

class SelflessHeroDrGold(BuffDeathrattle):
    name = "selfess_hero_dr_gold"
    text = "Give two random friendly minions Divine Shield."
    
    
    def __init__(self, minion):
        super().__init__(minion)
    
    
    def run(self, manager):
        owner = self.minion.boardNumber
        targets = manager.get_player_board(owner).minions
        if len(targets) > 0:
            target  = random.choice(targets)
            target.hasDivineShield = True
            targets = [x for x in targets if x != target]
            if len(targets) > 0:
                target  = random.choice(targets)
                target.hasDivineShield = True
                
        else:
            pass


class HarvestGolemDr(SummonDeathrattle):
    name = "harvest_golem_dr"
    text = "Summon a 2/1 Damaged Golem"
    
    def __init__(self, minion):
        super().__init__(minion)
    
    
    def run(self, manager):
        minionToSpawn = manager.create_minion("Damaged Golem", isGold=False)
        super().summon_minion(minionToSpawn, manager)
    
    
class HarvestGolemDrGold(SummonDeathrattle):
    name = "harvest_golem_dr_gold"
    text = "Summon a 4/2 Damaged Golem"
    
    def __init__(self, minion):
        super().__init__(minion)
    
    
    def run(self, manager):
        minionToSpawn = manager.create_minion("Damaged Golem", isGold=True)
        super().summon_minion(minionToSpawn, manager)


class KindlyGrandmotherDr(SummonDeathrattle):
    name = "kindly_grandmother_dr"
    text = "Summon a 3/2 Big Bad Wolf"
    
    def __init__(self, minion):
        super().__init__(minion)
    
    
    def run(self, manager):
         minionToSpawn = manager.create_minion("Big Bad Wolf", isGold=False)
         super().summon_minion(minionToSpawn, manager)
     
     
class KindlyGrandmotherDrGold(SummonDeathrattle):
     name = "kindly_grandmother_dr_gold"
     text = "Summon a 6/4 Big Bad Wolf"
     
     def __init__(self, minion):
        super().__init__(minion)
     
     
     def run(self, manager):
          minionToSpawn = manager.create_minion("Big Bad Wolf", isGold=True)
          super().summon_minion(minionToSpawn, manager)


class KaboomBotDr(AttackDeathrattle):
    name = "kaboom_bot_dr"
    text = "Deal 4 damage to a random enemy minion."
    
    def __init__(self, minion):
        super().__init__(minion)
    
    
    def run(self, manager):
        targetBoard = 1 if self.minion.boardNumber == 2 else 2
        targets = manager.get_player_board(targetBoard).minions
        if len(targets) > 0:
            target = random.choice(targets)
            target.recieve_damage(4, damageSource=self.minion)
    

class KaboomBotDrGold(AttackDeathrattle):
    name = "kaboom_bot_dr_gold"
    text = "Deal 4 damage to two random enemy minions."
    
    def __init__(self, minion):
        super().__init__(minion)
    
    
    def run(self, manager):
        targetBoard = 1 if self.minion.boardNumber == 2 else 2
        targets = manager.get_player_board(targetBoard).minions
        if len(targets) > 0:
            target = random.choice(targets)
            target.recieve_damage(4, damageSource=self.minion)
            targets = [x for x in targets if x != target]
            if len(targets) > 0:
                target = random.choice(targets)
                target.recieve_damage(4, damageSource=self.minion)


class MountedRaptorDr(SummonDeathrattle):
    name = "mounted_raptor_dr"
    text = "Summon a random 1-cost minion."
    
    def __init__(self, minion):
        super().__init__(minion)
    
    
    def run(self, manager):
        conditions = {
            "Cost" : 1,
            "isGold" : False,
            }
        
        minionToSpawn = manager.create_random_minion(**conditions)
        super().summon_minion(minionToSpawn, manager)


class MountedRaptorDrGold(SummonDeathrattle):
    name = "mounted_raptor_dr_gold"
    text = "Summon two random 1-cost minions."
    
    def __init__(self, minion):
        super().__init__(minion)
    
    
    def run(self, manager):
        conditions = {
            "Cost" : 1,
            "isGold" : True,
            }
        
        minionToSpawn = manager.create_random_minion(**conditions)
        super().summon_minion(minionToSpawn, manager)
        minionToSpawn = manager.create_random_minion(**conditions)
        super().summon_minion(minionToSpawn, manager)


class RatPackDr(SummonDeathrattle):
    name = "rat_pack_dr"
    text = "Summon a number of 1/1 rats equal to this minions attack"
    
    def _init__(self, minion):
        super().__init__(self, minion)
    
    
    def run(manager):
        for i in range(minion.attack):
            minionToSpawn = manager.create_minion("Rat", isGold=False)
            super().summon_minion(minionToSpawn, manager)
    

class RatPackDrGold(SummonDeathrattle):
    name = "rat_pack_dr_gold"
    text = "Summon a number of 2/2 rats equal to this minions attack"
    
    def _init__(self, minion):
        super().__init__(self, minion)
    
    
    def run(manager):
        for i in range(minion.attack):
            minionToSpawn = manager.create_minion("Rat", isGold=True)
            super().summon_minion(minionToSpawn, manager)


class SpawnOfNzothDr(BuffDeathrattle):
    name = "spawn_of_nzoth_dr"
    text = "Give your minions +1/+1"
    
    def __init__(self, minion):
        super().__init__(minion)
    
    
    def run(manager):
        board = manager.get_player_board(self.minion.boardNumber)
        for minion in board.minions:
            minion.buffs.append(AttackBuff("Permenant", 1))
            minion.buffs.append(HealthBuff("Permenant", 1))


class SpawnOfNzothDrGold(BuffDeathrattle):
    name = "spawn_of_nzoth_dr_gold"
    text = "Give your minions +2/+2"
    
    def __init__(self, minion):
        super().__init__(minion)
    
    
    def run(manager):
        board = manager.get_player_board(self.minion.boardNumber)
        for minion in board.minions:
            minion.buffs.append(AttackBuff("Permenant", 2))
            minion.buffs.append(HealthBuff("Permenant", 2))



classList = [
    MecharooDr,
    MecharooDrGold,
    SelflessHeroDr,
    SelflessHeroDrGold,
    HarvestGolemDr,
    HarvestGolemDrGold,
    KindlyGrandmotherDr,
    KindlyGrandmotherDrGold,
    KaboomBotDr,
    KaboomBotDrGold,
    MountedRaptorDr,
    MountedRaptorDrGold,
    RatPackDr,
    RatPackDrGold,
    SpawnOfNzothDr,
    SpawnOfNzothDrGold,
    ]

deathrattles = {x.name: x for x in classList}


def get_deathrattle(name):
    return deathrattles[name]
    
