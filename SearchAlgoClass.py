import heapq
from EightPuzzleClass import Node

########### Search Statistic Functions ###########
class SearchStats:
    def __init__ (self):
        self.numNodesExpanded = 0
        self.maxQueueSize = 1

    def printFinal(self, currNode):
        print("==================================================" + '\n' + 
              "       Goal State achieved! Puzzle solved!        " + '\n' +
              "==================================================")
        print(self.numNodesExpanded, "nodes were expanded")
        print("Largest size of the queue was", self.maxQueueSize)   
        print("Solution is at Depth", currNode.depth)
        return

############### Search Algorithms ################
class SearchAlgo:

    # Uniform Cost Search -- Equivalent to Breadth-First Search (Constant Costs)
    # Idea: Enqueue nodes in order of cost and expand cheapest nodes (min-heap)
    #       ... it's just A* with heuristic = 0
    @staticmethod
    def uniformCost(puzzle):

        root = Node(puzzle.startState, None, 0, 0)                  # set heuristic to 0
        frontier = []                                               # priority queue
        tie = 0                                                     # for tie comparisons
        minCost = {root.state: 0}                                   # track cheapest cost from root to node
        heapq.heappush(frontier, (0, tie, root))                    # arrange min-heap by g(n)
        stats = SearchStats()

        while True:                                                 # loop until queue is empty
            # If queue is empty, no result was/can be found return FAILURE
            if (not frontier):
                return None

            # Otherwise we pop the front node, which has cheapest cost
            cost, _, node = heapq.heappop(frontier)

            # skip node if state was already discovered with cheaper cost
            if (minCost[node.state] < cost): 
                continue

            print("Current State with Best Cost -- g(n): ", cost)
            puzzle.printState(node.state)

            # If currState is Goal State... then yay (SUCCESS)
            if (puzzle.isGoalState(node.state)):
                stats.printFinal(node)
                return node

            # otherwise keep expanding
            stats.numNodesExpanded += 1

            for childState in puzzle.expand(node.state):
                newCost = cost + 1                                  # each move to new depth costs 1

                # if current child state is new or has cheaper cost, branch out here
                if (childState not in minCost) or (newCost < minCost[childState]):
                    minCost[childState] = newCost                   # update cheapest cost found
                    curr = Node(childState, node, newCost, 0)

                    tie += 1                                        # for ties
                    heapq.heappush(frontier, (newCost, tie, curr))  # enqueue child node

                    if (stats.maxQueueSize < len(frontier)):
                        stats.maxQueueSize = len(frontier)
        return None

    # A* (Misplaced Tile Heuristic)
    # Idea: Enqueue nodes in order of f(n) = g(n) + h(n) and expand cheapest nodes (min-heap)
    #       ... it's UCS with heuristics tracked
    @staticmethod
    def a_MisplacedTile(puzzle):
        root = Node(puzzle.startState, None, 0, puzzle.tilesMisplaced(puzzle.startState))
        frontier = []                                               # priority queue
        tie = 0                                                     # for tie comparisons
        minCost = {root.state: 0}                                   # track cheapest cost from root to node
        heapq.heappush(frontier, (root.f_n(), tie, root))           # arrange min-heap by f(n)
        stats = SearchStats()

        while True:                                                 # loop until queue is empty
            # If queue is empty, no result was/can be found return FAILURE
            if (not frontier):
                return None

            # Otherwise we pop the front node, which has cheapest f(n)
            f, _, node = heapq.heappop(frontier)

            # skip node if state was already discovered with cheaper cost
            if (minCost[node.state] < node.depth):
                continue

            print("Current State with Best Cost -- g(n): ", node.depth, ", h(n): ", node.heuristic,
                ", f(n): ", node.f_n())
            puzzle.printState(node.state)

            # If currState is Goal State... then yay (SUCCESS)
            if (puzzle.isGoalState(node.state)):
                stats.printFinal(node)
                return node

            # otherwise keep expanding
            stats.numNodesExpanded += 1

            for childState in puzzle.expand(node.state):
                newCost = node.depth + 1                            # each move to new depth costs 1

                # if current child state is new or has cheaper cost, branch out here
                if (childState not in minCost) or (newCost < minCost[childState]):
                    minCost[childState] = newCost                   # update cheapest cost found
                    h = puzzle.tilesMisplaced(childState)           # compute misplaced tile heuristic
                    curr = Node(childState, node, newCost, h)       # make child node

                    tie += 1                                        # for ties
                    heapq.heappush(frontier, (curr.f_n(), tie, curr))  # enqueue child node 

                    if (stats.maxQueueSize < len(frontier)):
                        stats.maxQueueSize = len(frontier)
        return None

    # A* (Manhattan Distance Heuristic)
    # Idea: Enqueue nodes in order of f(n) = g(n) + h(n) and expand cheapest nodes (min-heap)
    #       ... it's misplaced tile but h(n) is Manhattan distance (excluding blank)
    @staticmethod
    def a_ManhattanDH(puzzle):

        root = Node(puzzle.startState, None, 0, puzzle.manhatDist(puzzle.startState))
        frontier = []                                           # priority queue
        tie = 0                                                 # for tie comparisons
        minCost = {root.state: 0}                               # track cheapest g(n) found for each state
        heapq.heappush(frontier, (root.f_n(), tie, root))       # arrange min-heap by f(n)
        stats = SearchStats()

        while True:                                             # loop until queue is empty
            # If queue is empty, no result was/can be found return FAILURE
            if (not frontier):
                return None

            # Otherwise we pop the front node, which has cheapest f(n)
            f, _, node = heapq.heappop(frontier)

            # skip node if state was already discovered with cheaper cost
            if (minCost[node.state] < node.depth):
                continue

            print("Current State with Best Cost -- g(n): ", node.depth, ", h(n): ", node.heuristic,
                ", f(n): ", node.f_n())
            puzzle.printState(node.state)

            # If currState is Goal State... then yay (SUCCESS)
            if (puzzle.isGoalState(node.state)):
                stats.printFinal(node)
                return node

            # otherwise keep expanding
            stats.numNodesExpanded += 1

            for childState in puzzle.expand(node.state):
                newCost = node.depth + 1                                # each move to new depth costs 1

                # if current child state is new or has cheaper cost, branch out here
                if (childState not in minCost) or (newCost < minCost[childState]):
                    minCost[childState] = newCost                       # update cheapest cost found
                    h = puzzle.manhatDist(childState)                   # compute manhattan heuristic
                    curr = Node(childState, node, newCost, h)           # make child node

                    tie += 1                                            # for ties
                    heapq.heappush(frontier, (curr.f_n(), tie, curr))   # enqueue child node

                    if (stats.maxQueueSize < len(frontier)):
                        stats.maxQueueSize = len(frontier)
        return None
