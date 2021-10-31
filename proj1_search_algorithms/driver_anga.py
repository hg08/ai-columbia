#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 11:29:58 2018

@author: huang
"""

from _collections import deque as q
import time
import resource
import sys
import math

class PuzzleState(object):
    """docstring for PuzzleState"""
    def __init__(self, config, n, parent=None, action="Initial", cost=0):
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
                self.blank_row = i / self.n
                self.blank_col = i % self.n
                break

    def display(self):

        for i in range(self.n):

            line = []

            offset = i * self.n

            for j in range(self.n):

                line.append(self.config[offset + j])

            print (line)

    def move_left(self):

        if self.blank_col == 0:

            return None

        else:

            blank_index = self.blank_row * self.n + self.blank_col

            target = blank_index - 1

            new_config = list(self.config)

            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]

            return PuzzleState(tuple(new_config), self.n, parent=self, action="Left", cost=self.cost + 1)

    def move_right(self):

        if self.blank_col == self.n - 1:

            return None

        else:

            blank_index = self.blank_row * self.n + self.blank_col

            target = blank_index + 1

            new_config = list(self.config)

            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]

            return PuzzleState(tuple(new_config), self.n, parent=self, action="Right", cost=self.cost + 1)

    def move_up(self):

        if self.blank_row == 0:

            return None

        else:

            blank_index = self.blank_row * self.n + self.blank_col

            target = blank_index - self.n

            new_config = list(self.config)

            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]

            return PuzzleState(tuple(new_config), self.n, parent=self, action="Up", cost=self.cost + 1)

    def move_down(self):
        if self.blank_row == self.n - 1:
            return None
        else:
            blank_index = self.blank_row * self.n + self.blank_col
            target = blank_index + self.n
            new_config = list(self.config)
            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]
            return PuzzleState(tuple(new_config), self.n, parent=self, action="Down", cost=self.cost + 1)

    def expand(self):
        """expand the node"""
        # add child nodes in order of UDLR
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

initial_state = [1,2,5,3,4,0,6,7,8]
goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def bfs_search(initial_state):
    """BFS search"""

    ### STUDENT CODE GOES HERE ###
    frontier = q(([PuzzleState(initial_state,3, None, 'Initial', 0)]))
    counter = 0
    explored = set()
    while frontier:
        state = frontier.popleft()
        explored.add(state)
        if state == goal_state:
            break
        neighbours = PuzzleState.expand(state)
        counter += 1
        for neighbor in neighbours:
           if neighbor not in explored:
               frontier.append(neighbor)
        print(counter)
    print (frontier)

def test_goal(puzzle_state):
    """test the state is the goal state or not"""
    ### S HERE ###
    goal_config = (0,1,2,3,4,5,6,7,8)
    #logging.info(type(puzzle_state.config))
    #logging.info(type(goal_state))
    #logging.info(puzzle_state.config)
    #logging.info(goal_config)
    if puzzle_state.config == goal_config:
        #logging.info('Result:'+ str(True))
        return True
    else:
        #logging.info('Result:'+ str(False))
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
    f.write('Manhattan distance:' + str(calculate_manhattan_dist(0, 7, 3))+'\n')
    f.write('Manhattan distance:' + str(calculate_manhattan_dist(1, 2, 3))+'\n')
    f.write('Manhattan distance:' + str(calculate_manhattan_dist(2, 4, 3))+'\n')
    print("Results are in 'output.txt'.")
