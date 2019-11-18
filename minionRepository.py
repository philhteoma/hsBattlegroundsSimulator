from minion import Minion
import csv

def parse_bool(string):
    if string == "True":
        return True
    elif string == "False":
        return False
    else:
        raise ValueError("String must be either 'True' or 'False'")

types = {
    "Name" : str,
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
        for rawMinion in self.rawMinions:
            minionSpec = {}
            for i in range(len(rawMinion)):
                specName = self.header[i]
                dataType = types[specName]
                dataValue = dataType(rawMinion[i])
                minionSpec[specName] = dataValue
            self.minionSpecs[minionSpec["Name"]] = minionSpec
    
    
    def create_minion(self, name):
        specs = self.minionSpecs[name]
        specs["Id"] = self._get_id()
        return Minion(self.minionSpecs[name])
        
        
    def _get_id(self):
        newId = self.currentId
        self.currentId += 1
        return newId
