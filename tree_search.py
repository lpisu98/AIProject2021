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
        if(problem.goal_test(node) == True):
            return node

        for n in expand(node, problem):
            fringe.append(n)

def depthFirstSearch(problem):
    iteration=0
    fringe = []
    fringe.append(Node(problem.initial_state))

    while 1:
        iteration+=1
        if(iteration % 1000 == 0):
            iteration=0
            print(iteration)
        if(len(fringe) == 0):
            return -1

        node = fringe.pop() #gives us the last element
        if(problem.goal_test(node) == True):
            return node

        new_nodes = expand(node, problem)

        if(new_nodes == []):
            node.parent_node.children_nodes.remove(node)

        for n in new_nodes:
            if(n != node.parent_node):
                fringe.append(n)
            #else : discard


def aStarSearch(problem):
    fringe = []
    fringe.append(Node(problem.initial_state))

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
        if(problem.goal_test(node) == True):
            return node

        for n in expand(node, problem):
            fringe.append(n)


def expand(node, problem):
    successors = []
    skip = False
    for (action, result) in problem.successor_fn(node.state):
        actual = node
        for i in range(node.depth):
            actual = actual.parent_node
            if (actual != None and result[0] == actual.state):
                skip = True # skip this iteration so that we don't add repeated states
                break

        if(not skip):
            n = Node()
            n.state = result[0]
            n.parent_node = node
            n.action = action
            n.path_cost = node.path_cost + problem.step_cost(node, action)
            n.depth = node.depth + 1
            n.children_nodes = []
            node.children_nodes.append(n)
            successors.append(n)
        skip = False

    return  successors

'''

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
'''