from minion import Minion
from playerBoard import PlayerBoard
from minionRepository import MinionRepository

def print_playerBoard(board):
    strings = [get_minion_print_strings(x) for x in board.minions]
    
    pivotStrings = []
    for i in range(len(strings[0])):
        lines = [x[i] for x in strings]
        unNest = [x for y in lines for x in y]
        pivotStrings.append("|" + "".join(unNest))
    
    print()
    print("\n".join(pivotStrings))
    print()
    
    for dr in board.deathrattles:
        print("{}-{} has deathrattle \"{}\"".format(dr.minion.name, dr.minion.id, dr.text))
    
    for se in board.staticEffects:
        print("{}-{} has static effect \"{}\"".format(se.minion.name, se.minion.id, se.text))
    
    for pe in board.personalEffects:
        print("{}-{} has personal effect \"{}\"".format(pe.minion.name, pe.minion.id, pe.text))
    
    print()

def get_minion_print_strings(minion):
    lineOne = minion.name + "-" + str(minion.id)
    lineTwo = "ATK:" + str(minion.attack) + " MaxH:" + str(minion.health) + " H:" + str(minion.currentHealth)
    lineThree = "".join([
        "T_" if minion.hasTaunt else "x_",
        "S_" if minion.hasDivineShield else "x_",
        "P" if minion.hasPoisonous else "x",
        ])
    combined = [lineOne, lineTwo, lineThree]
    
    maxLength = max([len(x) for x in combined])
    padded = [pad_string(x, maxLength) for x in combined]
    return padded
    

def pad_string(string, desiredLength):
    spacesToPad = desiredLength - len(string)
    leftPad = int(spacesToPad / 2)
    rightPad = spacesToPad - leftPad
    
    return " "*leftPad + string + " "*rightPad + "|"


if __name__ == "__main__":
    repo = MinionRepository(csvPath="static_data/minions.csv")
    board = PlayerBoard(boardNumber=1)
    
    board.add_minion_to_right(repo.create_minion("Micro Machine"))
    board.add_minion_to_right(repo.create_minion("Selfless Hero"))
    board.add_minion_to_right(repo.create_minion("Vulgar Homunculus"))
    board.add_minion_to_right(repo.create_minion("Mecharoo"))
    board.add_minion_to_right(repo.create_minion("Dire Wolf Alpha"))

    
    print_playerBoard(board)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
