#Search Agents
#Author: Gang
#=======
#Modules
#=======
import queue as Q  # For Python3
import time
import resource
import sys
import math
import os

#===============
# Initialization
#===============
cost_of_path = 0
nodes_expanded = 0
path_to_goal = []
set_search_depth = set()

#=====================================
# The Class that Represents the Puzzle
#=====================================
class PuzzleState(object):
    """The Class PuzzleState"""
    def __init__(self, config, n=3, parent=None, action="Initial", cost=0):
        if n*n != len(config) or n < 2:
            raise Exception("the length of config is not correct!")
        self.n = n
        self.cost = cost
        self.parent = parent
        self.action = action
        self.dimension = n
        self.config = config
        self.children = []

        for i, item in enumerate(self.config):
            if item == 0:
                self.blank_row = i // self.n
                self.blank_col = i % self.n
                break

    def display(self):
        for i in range(self.n):
            line = []
            offset = i * self.n
            for j in range(self.n):
                line.append(self.config[offset + j])
            print(line)

    def move_left(self):
        if self.blank_col == 0:
            return None
        else:
            blank_index = int(self.blank_row * self.n + self.blank_col)
            target = blank_index - 1
            new_config = list(self.config)
            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]
            return PuzzleState(tuple(new_config), self.n, parent=self, action="Left", cost=self.cost + 1)

    def move_right(self):
        if self.blank_col == self.n - 1:
            return None
        else:
            blank_index = int(self.blank_row * self.n + self.blank_col)
            target = blank_index + 1
            new_config = list(self.config)
            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]
            return PuzzleState(tuple(new_config), self.n, parent=self, action="Right", cost=self.cost + 1)

    def move_up(self):
        if self.blank_row == 0:
            return None
        else:
            blank_index = int(self.blank_row * self.n + self.blank_col)
            #print('blank_index:',blank_index)
            target = blank_index - self.n
            #print('target:',target)
            new_config = list(self.config)
            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]
            return PuzzleState(tuple(new_config), self.n, parent=self, action="Up", cost=self.cost + 1)

    def move_down(self):
        if self.blank_row == self.n - 1:
            return None
        else:
            blank_index = int(self.blank_row * self.n + self.blank_col)
            target = blank_index + self.n
            new_config = list(self.config)
            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]
            return PuzzleState(tuple(new_config), self.n, parent=self, action="Down", cost=self.cost + 1)

    def expand(self):
        """expand the node. Here we add child nodes in order of UDLR."""
        if len(self.children) == 0:
            up_child = self.move_up()

            if up_child is not None:
                self.children.append(up_child)
            down_child = self.move_down()

            if down_child is not None:
                self.children.append(down_child)
            left_child = self.move_left()

            if left_child is not None:
                self.children.append(left_child)
            right_child = self.move_right()

            if right_child is not None:
                self.children.append(right_child)
        return self.children

    def expand_reverse(self):
        """expand the node. Here we add child nodes in order of reverse-UDLR."""
        if len(self.children) == 0:
            right_child = self.move_right()

            if right_child is not None:
                self.children.append(right_child)
            left_child = self.move_left()

            if left_child is not None:
                self.children.append(left_child)
            down_child = self.move_down()

            if down_child is not None:
                self.children.append(down_child)
            up_child = self.move_up()

            if up_child is not None:
                self.children.append(up_child)
        return self.children

# Function that calculates path_to_goal
def calculate_path_to_goal(state,cost_of_path):
    path=[]
    path.append(state.action)
    x = state
    for i in range(cost_of_path):
        x = x.parent
        path.append(x.action)
    # path[::-1] gives the reversed list
    return path[::-1]

def bfs_search(initial_state):
    """BFS search"""

    # Global varialbles
    global cost_of_path,nodes_expanded,path_to_goal
    global set_search_depth # for calculating max_search_depth

    frontier = Q.Queue()
    frontier.put(initial_state)
    frontier_config = set()

    explored_queue = Q.Queue()

    # Create a new set: explored
    explored = set()
    explored_config = set()

    # Create a list for search_path
    search_path=[]

    while not frontier.empty():
        state = frontier.get() # choose the shallowest node
        explored.add(state)
        set_search_depth.add(state.cost)
        explored_queue.put(state)
        explored_config.add(state.config)
        search_path.append(state.action)

        if test_goal(state):
            # Calculate cost_of_path
            cost_of_path = calculate_total_cost(state)

            # Calculate num. of nodes expanded (exclude the initial state,therefore -1)
            nodes_expanded = len(explored)-1
            #print('search_path:',search_path[1:])

            # Calculate path_to_goal
            # use [1:] because we want to skip the 'Initial'
            path_to_goal = calculate_path_to_goal(state,cost_of_path)[1:]

            return "SUCCESS"

        for neighbor in state.expand():
            if (neighbor.config not in frontier_config) and \
            (neighbor.config not in explored_config):
                frontier.put(neighbor)
                frontier_config.add(neighbor.config)
    return "FAILURE"

def dfs_search(initial_state):
    """DFS search"""
    # Declare the global variables
    global cost_of_path,nodes_expanded,path_to_goal,\
           set_search_depth

    # The stack
    frontier = Q.LifoQueue()
    frontier._put(initial_state)
    frontier_config = set()

    # create a new set and a new LifoQueue: explored,explored_LifoQueue
    explored = set()
    explored_LifoQueue = Q.LifoQueue()
    explored_config = set()

    # create a list for search_path
    search_path=[]

    while frontier._qsize():
        state = frontier._get()
        set_search_depth.add(state.cost)
        explored.add(state)
        explored_LifoQueue._put(state)
        explored_config.add(state.config)
        search_path.append(state.action)

        if test_goal(state):
            #print 'cost_of_path'
            cost_of_path = calculate_total_cost(state)

            #the number of nodes expanded
            nodes_expanded = len(explored)-1
            #print('search_path:',search_path[1:])

            # Calculate path_to_goal
            # use [1:] because we want to skip the 'Initial'
            path_to_goal = calculate_path_to_goal(state,cost_of_path)[1:]

            return "SUCCESS"
        for neighbor in state.expand_reverse():
            if (neighbor.config not in frontier_config) and (neighbor.config not in explored_config):
                frontier.put(neighbor)
                frontier_config.add(neighbor.config)
    return "FAILURE"

def A_star_search(initial_state,goal_state):
    """A * search"""
    ### S HERE ###
    global cost_of_path,nodes_expanded,path_to_goal,\
           set_search_depth,n

    #frontier = Q.PriorityQueue()  #
    #frontier._put(initial_state)
    frontier = set() #
    frontier.add(initial_state)
    frontier_config = set() # The open set 2
    explored = set() # The close set
    explored_config =set()
    m = n*n

    # While Openset is not empty
    while frontier._qsize():
        state = frontier._get() # get the node in openset having the lowest f_score[] value
        explored = frontier._put(state)

        if test_goal(state):
            cost_of_path = calculate_total_cost(state)
            nodes_expanded = len(explored)-1
            path_to_goal = calculate_path_to_goal(state,cost_of_path)[1:]
            return "SUCCESS"

        for neighbor in state.expand():
            if neighbor.config in explored_config:
                pass
            tentative_g_score = g_score(state) + distance(state,neighbor)
            if neighbor.config not in frontier_config:
                frontier._put(neighbor)
                frontier_config.add(neighbor.config)
                tentative_is_better = True
            elif tentative_g_score < g_score[neighbor]:
                tentative_is_better = True
            else:
                tentative_is_better = False
            if tentative_is_better == True:
                pass
    return "FAILURE"

def calculate_total_cost(state):
    """calculate the total estimated cost of a state"""
    return state.cost

def calculate_manhattan_dist(idx, value, n):
    """calculatet the manhattan distance of a tile"""
    # Initialize the manhattan distance, h
    h = 0
    # The current row and col
    current_row_col = [idx//n, idx%n]

    ideal_row_col = [value//n, value%n]
    h += abs(current_row_col[0]-ideal_row_col[0]) + \
         abs(current_row_col[1]-ideal_row_col[1])
    return h

def test_goal(puzzle_state):
    """test the state is the goal state or not"""
    goal_config = (0,1,2,3,4,5,6,7,8)
    if puzzle_state.config == goal_config:
        return True
    else:
        return False

# Main Function that reads in Input and Runs corresponding Algorithm

def main():
    sm = sys.argv[1].lower()
    begin_state = sys.argv[2].split(",")
    begin_state = tuple(map(int, begin_state))
    size = int(math.sqrt(len(begin_state)))
    hard_state = PuzzleState(begin_state, size)
    if sm == "bfs":
        bfs_search(hard_state)
    elif sm == "dfs":
        dfs_search(hard_state)
    elif sm == "ast":
        A_star_search(hard_state)
    else:
        print("Enter valid command arguments !")

#get memory_usage
def max_ram_usage():
    unit = 1024.0
    usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / unit
    return usage

if __name__ == '__main__':
    start_time = time.time()
    main()
    running_time = round(time.time() - start_time,8)
    f = open('output.txt', 'w')
    f.write('path_to_goal:'+str(path_to_goal)+'\n')
    f.write('cost_of_path:'+str(cost_of_path)+'\n')
    f.write('nodes_expanded:'+str(nodes_expanded)+'\n')
    f.write('search_depth:'+str(cost_of_path)+'\n')
    f.write('max_search_depth:'+str(max(set_search_depth))+'\n')
    f.write('running_time:'+str(running_time)+'\n')
    f.write('max_ram_usage:'+str(max_ram_usage())+'\n')
    print("Results are in 'output.txt'.")
