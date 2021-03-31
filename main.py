import sys
from pathlib import Path


from route_finding import City, RouteFindingUtils
from tree_search import Problem, SearchStrategies
from puzzle_game import PuzzleGame, PuzzleGameUtils
import pickle
import time

# increase recursion limit to avoid exceptions during the algorithm execution
max_rec = 0x100000
sys.setrecursionlimit(max_rec)

# creation of the cities for Route Finding
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

# populating the cities with neighbors and distances
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

# create a list of the starting cities for the algorithm
cities = []
cities.append(oradea)
cities.append(zerind)
cities.append(arad)
cities.append(timisoara)
cities.append(lugoj)
cities.append(mehadia)
cities.append(drobeta)
cities.append(sibiu)
cities.append(rimnicu_vilcea)
cities.append(craiova)
cities.append(fagaras)
cities.append(pitesti)
cities.append(giurgiu)
cities.append(bucharest)
cities.append(neamt)
cities.append(iasi)
cities.append(vaslui)
cities.append(hirsova)
cities.append(eforie)

# problem initialization
problem = Problem()
problem.initial_state = arad
problem.goal_test = lambda n : n.state.name == "Bucharest"
problem.successor_fn = RouteFindingUtils.successor_fn
problem.step_cost = RouteFindingUtils.step_cost
problem.heuristic_fn = RouteFindingUtils.heuristic_fn

# for every city in the list execute the algorithm with Bucharest as destination
for city in cities:
    problem.initial_state = city

    start_time = time.process_time()
    res = SearchStrategies.breadthFirstSearch(problem)
    print(problem.initial_state.name, "to Bucharest")
    print("--- %s seconds ---" % (time.process_time() - start_time), "Route Finding - Breadth First!")
    file = open("obj.txt", "wb")
    pickle.dump(res, file)
    file.close()
    print("size of the tree:", Path('./obj.txt').stat().st_size, "bytes")
    print("Path cost of the solution:", res.path_cost)
    print("Depth of the solution:", res.depth)
    print("-------------------------------------------------------------")

    start_time = time.process_time()
    res = SearchStrategies.depthFirstSearch(problem)
    print("--- %s seconds ---" % (time.process_time() - start_time), "Route Finding - Depth First!")
    file = open("obj.txt", "wb")
    pickle.dump(res, file)
    file.close()
    print("size of the tree:", Path('./obj.txt').stat().st_size, "bytes")
    print("Path cost of the solution:", res.path_cost)
    print("Depth of the solution:", res.depth)
    print("-------------------------------------------------------------")

    start_time = time.process_time()
    res = SearchStrategies.aStarSearch(problem)
    print("--- %s seconds ---" % (time.process_time() - start_time), "Route Finding - A* search!")
    file = open("obj.txt", "wb")
    pickle.dump(res, file)
    file.close()
    print("size of the tree:", Path('./obj.txt').stat().st_size, "bytes")
    print("Path cost of the solution:", res.path_cost)
    print("Depth of the solution:", res.depth)
    print("-------------------------------------------------------------")

print("------------ Puzzle Game -------------------------------")

# creating a list of the puzzle game istances to be solved
games = []
games.append(PuzzleGame([[-1,2,3],[5,1,6],[4,8,7]]))
games.append(PuzzleGame([[1,3,8],[7,-1,5],[6,2,4]]))
games.append(PuzzleGame([[1,2,6],[4,5,8],[-1,7,3]]))
games.append(PuzzleGame([[7,1,2],[4,-1,6],[5,3,8]]))
games.append(PuzzleGame([[4,1,3],[8,7,5],[2,6,-1]]))
games.append(PuzzleGame([[5,7,2],[1,4,8],[-1,6,3]]))
games.append(PuzzleGame([[4,8,-1],[3,6,1],[7,2,5]]))
games.append(PuzzleGame([[-1,1,2],[4,6,3],[7,5,8]]))
games.append(PuzzleGame([[1,5,2],[3,-1,6],[8,4,7]]))
games.append(PuzzleGame([[8,6,5],[1,7,2],[4,3,-1]]))

# changing problem instance to be puzzle game
problem.goal_test = lambda n : n.state.grid == [[1,2,3],[4,5,6],[7,8,-1]]
problem.successor_fn = PuzzleGameUtils.successor_fn
problem.step_cost = PuzzleGameUtils.step_cost
problem.heuristic_fn = PuzzleGameUtils.heuristic_misplaced

# for every game board execute the algorithms
for game in games:
    problem.initial_state = game
    print(game.grid)

    start_time = time.process_time()
    res = SearchStrategies.breadthFirstSearch(problem)
    print("--- %s seconds ---" % (time.process_time() - start_time), "8 Puzzle Game - Breadth First!")
    file = open("obj.txt", "wb")
    pickle.dump(res, file)
    file.close()
    print("size of the tree:",Path('./obj.txt').stat().st_size, "bytes")
    print("Path cost of the solution:", res.path_cost)
    print("Depth of the solution:", res.depth)
    print("-------------------------------------------------------------")

    start_time = time.process_time()
    res = SearchStrategies.depthFirstSearch(problem)
    print("--- %s seconds ---" % (time.process_time() - start_time), "8 Puzzle Game - Depth First!")
    file = open("obj.txt", "wb")
    pickle.dump(res, file)
    file.close()
    print("size of the tree:",Path('./obj.txt').stat().st_size, "bytes")
    print("Path cost of the solution:", res.path_cost)
    print("Depth of the solution:", res.depth)
    print("-------------------------------------------------------------")

    problem.heuristic_fn = PuzzleGameUtils.heuristic_misplaced
    start_time = time.process_time()
    res = SearchStrategies.aStarSearch(problem)
    print("--- %s seconds ---" % (time.process_time() - start_time), "8 Puzzle Game - A* Search! - Misplaced tiles heuristic")
    file = open("obj.txt", "wb")
    pickle.dump(res, file)
    file.close()
    print("size of the tree:",Path('./obj.txt').stat().st_size, "bytes")
    print("Path cost of the solution:", res.path_cost)
    print("Depth of the solution:", res.depth)
    print("-------------------------------------------------------------")

    problem.heuristic_fn = PuzzleGameUtils.heuristic_manhattan
    start_time = time.process_time()
    res = SearchStrategies.aStarSearch(problem)
    print("--- %s seconds ---" % (time.process_time() - start_time), "8 Puzzle Game - A* Search! - Manhattan Heuristic")
    file = open("obj.txt", "wb")
    pickle.dump(res, file)
    file.close()
    print("size of the tree:",Path('./obj.txt').stat().st_size, "bytes")
    print("Path cost of the solution:", res.path_cost)
    print("Depth of the solution:", res.depth)
    print("-------------------------------------------------------------")




