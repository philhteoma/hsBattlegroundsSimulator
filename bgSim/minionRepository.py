from bgSim.minion import Minion
import csv
import random

def parse_bool(string):
    if string == "True":
        return True
    elif string == "False":
        return False
    else:
        raise ValueError("String must be either 'True' or 'False', not '{}'".format(string))

types = {
    "Name" : str,
    "Cost" : int,
    "Tier" : int,
    "Tribe" : str,
    "Attack" : int,
    "Health" : int,
    "Taunt" : parse_bool,
    "Poison" : parse_bool,
    "Shield" : parse_bool,
    "Deathrattle" : str,
    "StaticEffect" : str,
    "PersonalEffect" : str,
    "Token" : parse_bool,
    "isGold" : parse_bool,
    }

class MinionRepository:
    def __init__(self, csvPath):
        self.currentId = 1
        
        with open(csvPath, "r") as csvFile:
            minionReader = csv.reader(csvFile, delimiter=",")
            self.rawMinions = []
            for l in minionReader:
                self.rawMinions.append(l)

        self.header = self.rawMinions.pop(0)

        self.minionSpecs = {}
        self.goldMinionSpecs = {}
        for rawMinion in self.rawMinions:
            minionSpec = {}
            for i in range(len(rawMinion)):
                specName = self.header[i]
                dataType = types[specName]
                dataValue = dataType(rawMinion[i])
                minionSpec[specName] = dataValue
            for trait in ["Deathrattle", "StaticEffect", "PersonalEffect"]:
                minionSpec["has{}".format(trait)] = False if minionSpec[trait] == "" else True
            
            if minionSpec["isGold"]:
                self.goldMinionSpecs[minionSpec["Name"]] = minionSpec
            else:
                self.minionSpecs[minionSpec["Name"]] = minionSpec
    
    
    def create_minion(self, name, isGold=False):
        if isGold:
            specs = self.goldMinionSpecs[name]
        else:
            specs = self.minionSpecs[name]
        specs["Id"] = self._get_id()
        return Minion(specs)
        
        
    def _get_id(self):
        newId = self.currentId
        self.currentId += 1
        return newId
    
    
    def create_random_minion(self, **traits):
        traits["Token"] = False
        if traits["isGold"]:
            validSpecs = list(self.goldMinionSpecs.items())
        else:
            validSpecs = list(self.minionSpecs.items())
        for trait, value in traits.items():
            validSpecs = list(filter(lambda spec: spec[1][trait] == value, validSpecs))
        
        choice = random.choice([x[1] for x in validSpecs])
        choice["Id"] = self._get_id()
        return Minion(choice)
