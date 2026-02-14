from EightPuzzleClass import EightPuzzle
from SearchAlgoClass import SearchAlgo

################## Test Cases ####################
depth0 = [[1, 2, 3],                    
          [4, 5, 6], 
          [7, 8, 0]]
depth2 = [[1, 2, 3],                    # super easy (quickplay tester)
          [4, 5, 6], 
          [0, 7, 8]]
depth4 = [[1, 2, 3],                    # easy ish
          [5, 0, 6], 
          [4, 7, 8]]
depth8 = [[1, 3, 6],                  
          [5, 0, 2], 
          [4, 7, 8]]
depth16 = [[1, 6, 7],                   # med
          [5, 0, 3], 
          [4, 8, 2]]
depth24 = [[0, 7, 2],                   # hard
          [4, 6, 1], 
          [3, 5, 8]]
depth26 = [[0, 4, 7],                   # X-hard
           [8, 6, 2], 
           [5, 1, 3]]
depth31 = [[8, 6, 7],                   # limit
           [2, 5, 4],
           [3, 0, 1]]

################ Search Algorithms ################
def callUCSearch(puzzle):
    print("==================================================" + '\n' + 
          "   Solving Puzzle with Uniformed Cost Search...   " + '\n' +
          "==================================================")
    result = SearchAlgo.uniformCost(puzzle)
    return

def callA_MTSearch(puzzle):
    print("==================================================" + '\n' + 
          " Solving Puzzle with A* (Misplaced Tile) Search..." + '\n' +
          "==================================================")
    result = SearchAlgo.a_MisplacedTile(puzzle)
    return

def callA_MDHSearch(puzzle):
    print("==================================================" + '\n' + 
          "   Solving Puzzle with A* (Manhattan) Search...   " + '\n' +
          "==================================================")
    result = SearchAlgo.a_ManhattanDH(puzzle)
    return

################ General Functions ################
def main():
    start()
    return

def start():
    print("==================================================" + '\n' + 
          "         Starting Sliding Puzzle Solver...        " + '\n' +
          "==================================================" + '\n' +
          "  Enter char corresponding to desired GAMEMODE:   " + '\n' +
          "        (1)  --  Quickplay                        " + '\n' +
          "        (2)  --  Preset Puzzles                   " + '\n' +
          "        (3)  --  Custom Puzzle                    " + '\n' +
          "==================================================")
    startPuzzle = input("USER INPUT: ") 

    if (startPuzzle == "1"):
        callUCSearch(EightPuzzle(depth2))
        
    elif (startPuzzle == "2"):
        playPresets()

    elif (startPuzzle == "3"):    
        playCustom()

    return

def searchSelection(puzzle):
    print("==================================================" + '\n' + 
          "   Enter char corresponding to desired SEARCH:    " + '\n' +
          "    (1)  --  Uniform Cost Search                  " + '\n' +
          "    (2)  --  A* (Misplaced Tile)                  " + '\n' +
          "    (3)  --  A* (Manhattan Distance Heuristic)    " + '\n' +
          "    (q)  --  Go back to Main Menu                 " + '\n' +
          "==================================================")    
    searchSelected = input("USER INPUT: ")

    if (searchSelected == "1"):
        callUCSearch(puzzle)

    elif (searchSelected == "2"):
        callA_MTSearch(puzzle)

    elif (searchSelected == "3"):
        callA_MDHSearch(puzzle)

    elif (searchSelected == "q"):
        start()
    
    return

def playPresets():
    print("==================================================" + '\n' + 
          "            PRESET PUZZLES SELECTED!              " + '\n' +
          "   Enter char corresponding to desired PRESET:    " + '\n' +
          "           (1)  --  Easy                          " + '\n' +
          "           (2)  --  Medium                        " + '\n' +
          "           (3)  --  Hard                          " + '\n' +
          "           (4)  --  Extra Hard                    " + '\n' +
          "           (5)  --  Maximum Limit                 " + '\n' +
          "           (q)  --  Go back to Main Menu          " + '\n' +
          "==================================================")    
    presetSelected = input("USER INPUT: ")

    if (presetSelected == "1"):
        searchSelection(EightPuzzle(depth4))

    elif (presetSelected == "2"):
        searchSelection(EightPuzzle(depth16))

    elif (presetSelected == "3"):
        searchSelection(EightPuzzle(depth24))

    elif (presetSelected == "4"):
        searchSelection(EightPuzzle(depth28))

    elif (presetSelected == "5"):
        searchSelection(EightPuzzle(depth31))

    # to test
    # if (presetSelected == "1"):
    #     searchSelection(EightPuzzle(depth0))

    # elif (presetSelected == "2"):
    #     searchSelection(EightPuzzle(depth2))

    # elif (presetSelected == "3"):
    #     searchSelection(EightPuzzle(depth4))

    # elif (presetSelected == "4"):
    #     searchSelection(EightPuzzle(depth8))

    # elif (presetSelected == "5"):
    #     searchSelection(EightPuzzle(depth16))

    # elif (presetSelected == "6"):
    #     searchSelection(EightPuzzle(depth24))

    # elif (presetSelected == "7"):
    #     searchSelection(EightPuzzle(depth26))

    # elif (presetSelected == "8"):
    #     searchSelection(EightPuzzle(depth31))

    elif (presetSelected == "q"):
        start()

    return

def playCustom():
    print("==================================================" + '\n' + 
          "            CUSTOM PUZZLES SELECTED!              " + '\n' +
          "  Enter puzzle row by row. Only distinct numbers  " + '\n' +
          "    from 0-8 inclusive allowed. Use spaces in     " + '\n' +
          "    between. Use '0' to define blank in puzzle.   " + '\n' +
          "==================================================")
       
    customRow1 = input("(Row 1) USER INPUT: ")
    customRow1 = customRow1.split()
    customRow2 = input("(Row 2) USER INPUT: ")
    customRow2 = customRow2.split()
    customRow3 = input("(Row 3) USER INPUT: ")
    customRow3 = customRow3.split()

    for i in range (0, 3):
        customRow1[i] = int(customRow1[i])
        customRow2[i] = int(customRow2[i])
        customRow3[i] = int(customRow3[i])

    customPuzzle = [customRow1, customRow2, customRow3]
    searchSelection(EightPuzzle(customPuzzle))
    
    return

if (__name__ == "__main__"): # 
    main()
