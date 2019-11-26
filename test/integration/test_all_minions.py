from bgSim.minionRepository import MinionRepository

minionsToTest = [
    "Alleycat","Tabbycat","Dire Wolf Alpha","Mecharoo","Jo-E Bot",
    "Micro Machine","Murloc Tidecaller","Murloc Tidehunter","Murloc Scout","Righteous Protector",
    "Rockpool Hunter","Selfless Hero","Voidwalker","Vulgar Homunculus","Wrath Weaver",
    
    "Annoy-o-Tron","Coldlight Seer","Harvest Golem","Damaged Golem","Kaboom Bot",
    "Kindly Grandmother","Big Bad Wolf","Metaltooth Leaper","Mounted Raptor","Murloc Warleader",
    "Nathrezim Overseer","Nightmare Amalgam","Old Murk-Eye","Pogo-Hopper","Rat Pack",
    "Rat","Shielded Minibot","Spawn of N'Zoth","Zoobot",
    ]

def test_all_minions():
    repo = MinionRepository(csvPath="static_data/minions.csv")
    
    for minion in minionsToTest:
        newMinion = repo.create_minion(minion)
    
    for minion in minionsToTest:
        newMinion = repo.create_minion(minion, isGold=True)
