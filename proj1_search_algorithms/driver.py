#import queue as Q  # in Python3, use lower case queue

import time
import resource
import sys
import math
import os
import logging

filename = 'info.log'
try:
    os.remove(filename)
except OSError:
    pass
logging.basicConfig(filename=filename,level=logging.INFO)
## The Class that Represents the Puzzle

class PuzzleState(object):

    """docstring for PuzzleState"""

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
            print('blank_index:',blank_index)
            target = blank_index - self.n
            print('target:',target)
            new_config = list(self.config)
            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]
            return PuzzleState(tuple(new_config), self.n, parent=self, action="Up", cost=self.cost + 1)

    def move_down(self):
        if self.blank_row == self.n - 1:
            return None
        else:
            blank_index = int(self.blank_row * self.n + self.blank_col)
            print('blank_index:',blank_index)
            target = blank_index + self.n
            print('target:',target)
            new_config = list(self.config)
            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]
            return PuzzleState(tuple(new_config), self.n, parent=self, action="Down", cost=self.cost + 1)

    def expand(self):
        """expand the node"""  # add child nodes in order of UDLR
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
        """expand the node"""  # add child nodes in order of reverse-UDLR
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

# Function that Writes to output.txt

### Students need to change the method to have the corresponding parameters

def writeOutput(state):
    ### Student Code Goes here
    f = open('output.txt', 'a')
    cost_of_path = calculate_total_cost(state)
    f.write('cost_of_path = '+str(cost_of_path)+'\n')

def bfs_search(initial_state):
    """BFS search"""
    #to construct a class queue
    class Queue(object):
        def __init__(self, queue=None):
            if queue is None:
                self.queue = []
            else:
                self.queue = list(queue)
        def isEmpty(self):
            return self.queue == []
        def dequeue(self):
            return self.queue.pop(0)
        def enqueue(self, element):
            self.queue.append(element)
        def __contains__(self,item):
            return True if item in self.__dict__.keys() else False

    frontier = Queue()
    frontier.enqueue(initial_state)

    # create a new set: explored
    explored = set()
    # create a list for search_path
    search_path=[]
    #open a file 'output.txt'
    f = open('output.txt', 'w')

    n_expanded = 0

    while not frontier.isEmpty():
        state = frontier.dequeue() # choose the shallowest node
        explored.add(state)

        #to get the action sequence
        print('state.action:',state.action)
        search_path.append(state.action)

        if test_goal(state):
            print("SUCCESS")
            #print 'cost_of_path'
            writeOutput(state)
            #the number of nodes expanded
            nodes_explored = len(explored)
            print('nodes_explored:',nodes_explored)
            print('search_path:',search_path[1:])
            return "SUCCESS"
            #return success(state)
        for neighbor in state.expand():
            if (neighbor not in frontier) and (neighbor not in explored):
                #frontier.enqueue(neighbor)
                frontier.enqueue(neighbor)
                n_expanded += 1
        print('n_expanded:',n_expanded)
    print("FAILURE")
    return "FAILURE"

def dfs_search(initial_state):
    """DFS search"""

    #to construct a class stack
    class Stack(object):
        def __init__(self, stack=None):
            if stack is None:
                self.stack = []
            else:
                self.stack = list(stack)
        def isEmpty(self):
            return self.stack == []
        def pop(self):
            return self.stack.pop()
        def push(self, element):
            self.stack.append(element)
        def size(self):
            return len(self.stack)
        def peek(self):
            return self.stack[len(self.stack)-1]
        def __contains__(self,item):
            return True if item in self.__dict__.keys() else False

    frontier = Stack()
    logging.info("A stack is created.")
    frontier.push(initial_state)

    # create a new set: explored
    explored = set()
    logging.info("A set 'explored' is created.")
    # create a list for search_path
    search_path=[]
    #open a file 'output.txt'
    f = open('output.txt', 'w')
    logging.info("A file output.txt is created.")

    n_expanded = 0
    set_tmp = set()
    set_tmp1 = set()

    while not frontier.isEmpty():
        state = frontier.pop()
        print(state.action)
        logging.info("pop a state from the frontier.")
        explored.add(state)

        #to get the action sequence
        logging.info('state.action:'+str(state.action))
        search_path.append(state.action)

        if test_goal(state):
            logging.info("SUCCESS")
            #print 'cost_of_path'
            writeOutput(state)
            #the number of nodes expanded
            nodes_explored = len(explored)
            print('nodes_explored:',nodes_explored)
            print('search_path:',search_path[1:])
            return "SUCCESS"
        for i in range(frontier.size()):
            state = frontier.peek() # use peek to get info,but do not remove the elment
            set_tmp.add(state.config)
        for item in explored:
            set_tmp1.add(item.config)
        for neighbor in state.expand_reverse():
            if (neighbor.config not in set_tmp) and (neighbor.config not in set_tmp1):
                frontier.push(neighbor)
                n_expanded += 1
            print('n_expanded:',n_expanded)
    print("FAILURE")
    return "FAILURE"

def A_star_search(initial_state):
    """A * search"""
    ### S HERE ###
    pass
def calculate_total_cost(state):
    """calculate the total estimated cost of a state"""
    ### S HERE ###
    return state.cost
def calculate_manhattan_dist(idx, value, n):
    """calculatet the manhattan distance of a tile"""
    ### S HERE ###
    pass
def test_goal(puzzle_state):
    """test the state is the goal state or not"""
    ### S HERE ###
    goal_state = (0,1,2,3,4,5,6,7,8)
    logging.info(type(puzzle_state.config))
    logging.info(type(goal_state))
    logging.info(puzzle_state.config)
    logging.info(goal_state)
    if puzzle_state.config == goal_state:
        logging.info('Result:'+ str(True))
        return True
    else:
        print('Result:',False)
        logging.info(False)

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
    print("running_time:",running_time)
    print("max_ram_usage:",max_ram_usage())
    #li=[i for i in range(100000)]
    #li.append(10001)
    #print("after li: max_ram_usage:",max_ram_usage())
