class City:

    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def addNeighbor(self, city, cost):
        city.neighbors.append((city, cost))
        self.neighbors.append((city, cost))

class Node:

    def __init__(self):
        self.state = None
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

def treeSearch(problem):
    fringe = []
    fringe.append(Node(problem.initial_state))

    while 1:
        if(len(fringe) == 0):
            return -1

        node = fringe.pop()
        if(problem.goal_test(node) == True):
            return node

        fringe.append(expand(node, problem), fringe)

def expand(node, problem):
    successors = []
    for (action, result) in problem.successor_fn(node.state):
        n = Node()
        n.state = result
        n.parent_node = node
        n.action = action
        n.path_cost = node.path_cost + problem.step_cost(node, action)
        n.depth = node.depth + 1
        n.children_nodes = []
        node.children_nodes.append(n)
        successors.append(n)
    return  successors

def SF(state):
    res = []
    print(state.neighbors[0])
    for neighbor in state.neighbors:
        info = (neighbor.name, neighbor)
        res.append(info)

a = City("A")
b = City("B")
c = City("C")
d = City("D")

a.addNeighbor(b, 10)
b.addNeighbor(c, 15)
c.addNeighbor(d, 6)

problem = Problem()
problem.initial_state = a
problem.goal_test = lambda s : s.name == "D"
print(SF(a))


