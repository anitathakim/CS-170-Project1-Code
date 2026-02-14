################## Node Class ####################
class Node:
    def __init__ (self, state, parent = None, depth = 0, heuristic = 0):
        self.state = state
        self.depth = depth              # g(n) cost from initial to node
        self.parent = parent
        self.heuristic = heuristic      # h(n) estimated distance to goal 
    
    # Track f(n) of each node
    def f_n(self):
        return self.depth + self.heuristic

############# Eight Puzzle Object ################
class EightPuzzle:
    # Fixed Goal State
    goalState = ((1, 2, 3), 
                 (4, 5, 6),
                 (7, 8, 0))
    
    # Object initializer
    def __init__ (self, startState):
        self.startState = self.freezeState(startState) # convert to tuple

    # State checker
    def isGoalState(self, currState):
        if (isinstance(currState, list)): # if list, convert to tuple
            currState = self.freezeState(currState) 
        return currState == EightPuzzle.goalState # compare with goal state
    
    # List -> Tuple 
    def freezeState(self, currState):
        return tuple(tuple(i) for i in currState)   # ensures state is in tuple form for comparisons
    
    # Find position of blank in grid
    def findBlank(self, currState):
        for i in range (0, 3):
            for j in range (0, 3):
                if (currState[i][j] == 0):          # if curr element in grid == 0, 
                    return i, j                     # it's blank
        return # assume blank always exists in state
    
    # Print grid state
    def printState(self, currState):
        for i in currState:
            print(list(i))                          # print each row's list 

        return
    
    # Expands current state's variant possibilities 
    def expand(self, currState):
        if (isinstance(currState, list)):
            currState = self.freezeState(currState)
    
        variants = []
        moveset = [(1, 0),      # move blank down
                   (0, 1),      # move blank right
                   (-1, 0),     # move blank up
                   (0, -1)]     # move blank left
        currBlankRow, currBlankCol = self.findBlank(currState) # find blank position

        # spawn children
        for move_i, move_j in moveset:
            newBlankRow = currBlankRow + move_i
            newBlankCol = currBlankCol + move_j

            if (0 <= newBlankRow <= 2) and (0 <= newBlankCol <= 2): # if variant is valid, include it in expansion
                variants.append(self.buildVariant(currState, currBlankRow, currBlankCol, newBlankRow, newBlankCol))

        return variants
    
    # Generate variants of current state
    def buildVariant(self, currState, currBlank_i, currBlank_j, newBlank_i, newBlank_j):
        variantState = [list(i) for i in currState]

        # build a new state by swapping blank with neighbor
        variantState[currBlank_i][currBlank_j], variantState[newBlank_i][newBlank_j] = \
            variantState[newBlank_i][newBlank_j], variantState[currBlank_i][currBlank_j]
        
        return self.freezeState(variantState)
    
    # Compute tiles that must be moved to achieve goal state (heuristic)
    def tilesMisplaced(self, currState):
        totMisplaced = 0
        for i in range (0, 3):
            for j in range (0, 3):
                tile = currState[i][j]
                
                # if tile is not in goal state and tile is not blank, increment counter
                if (tile != EightPuzzle.goalState[i][j]) and (tile != 0):
                    totMisplaced += 1

        return totMisplaced
    
    # Compute manhattan distance (heuristic)
    def manhatDist(self, currState):
        totDist = 0
        for i in range (0, 3):
            for j in range (0, 3):
                tile = currState[i][j]
                
                if (tile != 0): # exclude blank tile
                    goal_i = (tile - 1) // 3    # tile's correct row position 
                    goal_j = (tile - 1) % 3     # tile's correct col position 
                    totDist += abs(i - goal_i) + abs(j - goal_j) # add curr&corr diff to h(n)

        return totDist