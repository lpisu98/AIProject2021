from route_finding import City, step_cost, successor_fn, heuristic_fn
from tree_search import Problem, treeSearch, aStarSearch

oradea = City("Oradea")
zerind = City("Zerind")
arad = City("Arad")
timisoara = City("Timisoara")
lugoj = City("Lugoj")
mehadia = City("Mehadia")
drobeta = City("Drobeta")
sibiu = City("Sibiu")
rimnicu_vilcea = City("Rimnicu Vilcea")
craiova = City("Craiova")
fagaras = City("Fagaras")
pitesti = City("Pitesti")
bucharest = City("Bucharest")
giurgiu = City("Giurgiu")
neamt = City("Neamt")
iasi = City("Iasi")
vaslui = City("Vaslui")
urziceni = City("Urziceni")
hirsova = City("Hirsova")
eforie = City("Eforie")

oradea.addNeighbor(zerind, 71)
oradea.addNeighbor(sibiu, 151)
zerind.addNeighbor(arad, 75)
arad.addNeighbor(sibiu, 140)
arad.addNeighbor(timisoara, 118)
timisoara.addNeighbor(lugoj, 111)
lugoj.addNeighbor(mehadia, 70)
mehadia.addNeighbor(drobeta, 75)
drobeta.addNeighbor(craiova, 120)
sibiu.addNeighbor(fagaras, 99)
sibiu.addNeighbor(rimnicu_vilcea, 80)
rimnicu_vilcea.addNeighbor(craiova, 146)
rimnicu_vilcea.addNeighbor(pitesti, 97)
craiova.addNeighbor(pitesti, 138)
fagaras.addNeighbor(bucharest, 211)
pitesti.addNeighbor(bucharest, 101)
bucharest.addNeighbor(giurgiu, 90)
bucharest.addNeighbor(urziceni, 98)
neamt.addNeighbor(iasi, 87)
iasi.addNeighbor(vaslui, 92)
vaslui.addNeighbor(urziceni, 142)
urziceni.addNeighbor(hirsova, 98)
hirsova.addNeighbor(eforie, 86)


problem = Problem()
problem.initial_state = arad
problem.goal_test = lambda n : n.state.name == "Bucharest"
problem.successor_fn = successor_fn
problem.step_cost = step_cost
problem.heuristic_fn = heuristic_fn

for city in arad.neighbors:
    print(city[0].name)

#res = treeSearch(problem)
res2 = aStarSearch(problem)
#print(res.path_cost)
#print(res.parent_node.state.name)
print(res2.path_cost)
#print(res2.parent_node.state.name)