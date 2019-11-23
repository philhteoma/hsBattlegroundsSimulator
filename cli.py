from bgSim.minion import Minion
from bgSim.playerBoard import PlayerBoard
from bgSim.minionRepository import MinionRepository
from bgSim.gameManager import GameManager

def print_playerBoard(board):
    if len(board.minions) > 0:
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
    else:
        print("Player {} board is empty".format(board.boardNumber))

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
    print(type(repo))
    manager = GameManager(repo)
    manager.assign_minion_to_board(repo.create_minion("Micro Machine"), 1)
    manager.assign_minion_to_board(repo.create_minion("Selfless Hero"), 1)
    manager.assign_minion_to_board(repo.create_minion("Mecharoo"), 2)
    manager.assign_minion_to_board(repo.create_minion("Dire Wolf Alpha"), 2)
    
    print("Starting Boards")
    print("------------------")
    print_playerBoard(manager.get_player_board(1))
    print()
    print_playerBoard(manager.get_player_board(2))
    print()

    
    manager.set_first_player()
    #manager.run_full_combat()
    
    print()
    print("Ending Boards")
    print("-----------------")
    print_playerBoard(manager.get_player_board(1))
    print()
    print_playerBoard(manager.get_player_board(2))
    print()
    
    
    """
    results = []
    for i in range(1):
        
        manager = GameManager(repo)
        manager.assign_minion_to_board(repo.create_minion("Micro Machine"), 1)
        manager.assign_minion_to_board(repo.create_minion("Selfless Hero"), 1)
        manager.assign_minion_to_board(repo.create_minion("Alleycat"), 2)
        manager.assign_minion_to_board(repo.create_minion("Dire Wolf Alpha"), 2)
        
        manager.set_first_player()
        manager.run_full_combat()
        
        if len(manager.get_player_board(1).minions) == 0:
            if len(manager.get_player_board(2).minions) == 0:
                r = "Tie"
            else:
                r = 2
        else:
            if len(manager.get_player_board(2).minions) == 0:
                r = 1
            else:
                r = "Error"
        results.append(r)
    
    print("1 : ", results.count(1))
    print("2 : ", results.count(2))
    print("Tie: ", results.count("Tie"))
    print("Error: ", results.count("Error"))
    """
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
