import queue as Q

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
            target = blank_index - self.n
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

def test_goal(puzzle_state):
    """test the state is the goal state or not"""
    goal_config = (0,1,2,3,4,5,6,7,8)
    if puzzle_state.config == goal_config:
        return True
    else:
        return False

def test_goal_beta(puzzle_state_config):
    """test the state is the goal state or not. The input is a tuple, instead a puzzle state."""
    goal_config = (0,1,2,3,4,5,6,7,8)
    if puzzle_state_config == goal_config:
        return True
    else:
        return False

# Function that calculates path_to_goal
def calculate_path_to_goal(state,cost_of_path):
    path = []
    path.append(state.action)
    x = state
    for i in range(cost_of_path):
        x = x.parent
        path.append(x.action)
    # path[::-1] gives the reversed list
    return path[::-1]

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

global cost_of_path,nodes_expanded,path_to_goal,\
           set_search_depth

frontier = Q.PriorityQueue()
#initial_state = 7,2,4,5,0,6,8,3,1
initial_state =0,1,2,3,4,5,6,7,8
#initial_state =3,1,2,0,4,5,6,7,8
goal_state = 0,1,2,3,4,5,6,7,8
initial_state = tuple(map(int, initial_state))
print("initial_state:",initial_state)
print("type of initial_state:",type(initial_state))
goal_state = tuple(map(int, goal_state))
size = 3
m = size * size
hard_state = PuzzleState(initial_state, size) # instance of initial state
goal_state = PuzzleState(goal_state, size)
print("hard_state:",hard_state)

g_score = 0
h_score = sum([calculate_manhattan_dist(list(goal_state.config)[i],list(hard_state.config)[i],size) for i in range(m)])
f_score = h_score
obj_state = [f_score, hard_state]
frontier._put(obj_state) # For the first element, it's correct to put obj_state into the frontier, with hard_state being a PuzzleState instance
print("type of hard_state",type(hard_state))
frontier_config = set()
explored = set()
explored_config = set()

# create a list for search_path
search_path=[]

while frontier:
    #frontier._put(2)
    x = frontier._get()
    print("AFTER _GET()!")
    print("first pop:",x)
    print("first pop's type:",type(x))
    print("x[-1] type:",type(x[-1])) # class
    x_state = x[-1]
    print("x_state:",x_state)
    print("WARNNING!")

    #x_state = tuple(map(int, x_state)) ##
    #x_state = PuzzleState(x_state, size)
    explored_config.add(x[-1].config)
    explored.add(x[-1])
    h_score = sum([calculate_manhattan_dist(list(goal_state.config)[i],list(x[-1].config)[i],size) for i in range(m)]) # h_score[start]
    print("h_score:",h_score)
    #x = frontier._get()
    #print("second pop:",x)

    if test_goal(x[-1]):
        print("SUCCESS")

        cost_of_path = calculate_total_cost(x_state)
        print("cost of path:",cost_of_path)
        #the number of nodes expanded
        nodes_expanded = len(explored)-1
        print("nodes_expanded:",nodes_expanded)
        #to get the action sequence
        #logging.info('state.action:'+str(state.action))

        search_path.append(x_state.action)
        print("search_path:",search_path)

        # Calculate path_to_goal
        # use [1:] because we want to skip the 'Initial'
        path_to_goal = calculate_path_to_goal(x_state,cost_of_path)[1:]
        print("path_to_goal:",path_to_goal)
    for neighbor in x[-1].expand():
        if neighbor in explored:
            pass
        tentative_g_score = g_score + \
        sum([calculate_manhattan_dist(list(neighbor.config)[i],list(x_state.config)[i],size) for i in range(m)])
        if neighbor.config not in frontier_config:
            g_score = sum([calculate_manhattan_dist(list(hard_state.config)[i],list(neighbor.config)[i],size) for i in range(m)])
            h_score = sum([calculate_manhattan_dist(list(goal_state.config)[i],list(neighbor.config)[i],size) for i in range(m)])
            f_score = g_score + h_score
            obj_state = [f_score, neighbor] # I should put the neighbor, as a node, into obj_state
            frontier._put(obj_state) # But _put() can not accept the neighbor as a node! What should I do to fix this problem?
            tentative_is_better = True
        elif tentative_g_score < g_score:
            tentative_is_better = True
        else:
            tentative_is_better = False
        if tentative_is_better == True:
            g_score = tentative_g_score
            h_score = sum([calculate_manhattan_dist(list(goal_state.config)[i],list(neighbor.config)[i],size) for i in range(m)])
            obj_state[0] = g_score + h_score

