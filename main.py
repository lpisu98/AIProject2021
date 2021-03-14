import sys
from pathlib import Path

from route_finding import City, RouteFindingUtils
from tree_search import Problem, treeSearch, aStarSearch, depthFirstSearch
from puzzle_game import PuzzleGame, PuzzleGameUtils
import pickle
import time

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
problem.successor_fn = RouteFindingUtils.successor_fn
problem.step_cost = RouteFindingUtils.step_cost
problem.heuristic_fn = RouteFindingUtils.heuristic_fn

start_time = time.time()
res = treeSearch(problem)
print("--- %s seconds ---" % (time.time() - start_time), "Route Finding - Breadth First!")
file = open("obj.txt", "wb")
pickle.dump(res, file)
file.close()
print("size of the tree:",Path('./obj.txt').stat().st_size, "bytes")

start_time = time.time()
res2 = aStarSearch(problem)
print("--- %s seconds ---" % (time.time() - start_time), "Route Finding - A* search!")
file = open("obj.txt", "wb")
pickle.dump(res2, file)
file.close()
print("size of the tree:",Path('./obj.txt').stat().st_size, "bytes")

start_time = time.time()
res3 = depthFirstSearch(problem)
print("--- %s seconds ---" % (time.time() - start_time), "Route Finding - Depth First!")
file = open("obj.txt", "wb")
pickle.dump(res3, file)
file.close()
print("size of the tree:",Path('./obj.txt').stat().st_size, "bytes")

game = PuzzleGame([[1,2,3],[4,5,6],[7,-1,8]])
problem.initial_state = game
problem.goal_test = lambda n : n.state.grid == [[1,2,3],[4,5,6],[7,8,-1]]
problem.successor_fn = PuzzleGameUtils.successor_fn
problem.step_cost = PuzzleGameUtils.step_cost
problem.heuristic_fn = PuzzleGameUtils.heuristic_fn

start_time = time.time()
res = aStarSearch(problem)
print("--- %s seconds ---" % (time.time() - start_time), "8 Puzzle Game - A* Search!")
file = open("obj.txt", "wb")
pickle.dump(res, file)
file.close()
print("size of the tree:",Path('./obj.txt').stat().st_size, "bytes")

start_time = time.time()
res = treeSearch(problem)
print("--- %s seconds ---" % (time.time() - start_time), "8 Puzzle Game - Breadth First!")
file = open("obj.txt", "wb")
pickle.dump(res, file)
file.close()
print("size of the tree:",Path('./obj.txt').stat().st_size, "bytes")

start_time = time.time()
res = depthFirstSearch(problem)
print("--- %s seconds ---" % (time.time() - start_time), "8 Puzzle Game - Depth First!")
file = open("obj.txt", "wb")
pickle.dump(res, file)
file.close()
print("size of the tree:",Path('./obj.txt').stat().st_size, "bytes")




