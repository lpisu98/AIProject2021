class Node:

    def __init__(self, state = None):
        self.state = state
        self.parent_node = None
        self.children_nodes = []
        self.action = ""
        self.path_cost = 0
        self.depth = 0

class Problem:

    def __init__(self):
        self.initial_state = None
        self.goal_test = None
        self.successor_fn = None
        self.step_cost = None
        self.heuristic_fn = None

def treeSearch(problem):
    fringe = []
    fringe.append(Node(problem.initial_state))

    while 1:
        if(len(fringe) == 0):
            return -1

        node = fringe.pop(0)
        print("Expanding ", node.state.name)
        if(problem.goal_test(node) == True):
            return node

        for n in expand(node, problem):
            fringe.append(n)

def aStarSearch(problem):
    fringe = []
    fringe.append(Node(problem.initial_state))
    min_node = None
    min_num = 0
    while 1:
        if(len(fringe) == 0):
            return -1

        min_node = fringe[0]
        min_num = min_node.path_cost + problem.heuristic_fn(fringe[0].state)
        for n in fringe[1:]:
            temp = problem.heuristic_fn(n.state)+n.path_cost
            if(temp < min_num):
                min_node = n
                min_num = temp

        node = min_node
        fringe.remove(node)
        print("Expanding ", node.state.name)
        if(problem.goal_test(node) == True):
            return node

        for n in expand(node, problem):
            fringe.append(n)

def expand(node, problem):
    successors = []
    for (action, result) in problem.successor_fn(node.state):
        if(node.parent_node != None and result[0] == node.parent_node.state):
            continue #skip this iteration so that we don't add repeated states
        n = Node()
        n.state = result[0]
        n.parent_node = node
        n.action = action
        n.path_cost = node.path_cost + problem.step_cost(node, action)
        n.depth = node.depth + 1
        n.children_nodes = []
        node.children_nodes.append(n)
        successors.append(n)
    return  successors

