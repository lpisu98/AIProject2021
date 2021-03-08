class City:

    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def addNeighbor(self, city, cost):
        city.neighbors.append((self, cost))
        self.neighbors.append((city, cost))

    def __eq__(self, other):
        return self.name == other.name

def heuristic_fn(state):
    values = {"Arad":366, "Bucharest":0, "Craiova":160, "Drobeta":242, "Eforie":161,
              "Fagaras":176, "Giurgiu": 77, "Hirsova":151, "Iasi":226, "Lugoj":244,
              "Mehadia":241, "Neamt":234, "Oradea":380, "Pitesti":100, "Rimnicu Vilcea":193,
              "Sibiu":253, "Timisoara":329, "Urziceni":80, "Vaslui":199, "Zerind":374}

    return values[state.name]

def successor_fn(state):
    res = []
    for neighbor in state.neighbors:
        info = (neighbor[0].name, neighbor)
        res.append(info)

    return res

def step_cost(node, action):
    for neighbor in node.state.neighbors:
        if (neighbor[0].name == action):
            return neighbor[1]
    return -1