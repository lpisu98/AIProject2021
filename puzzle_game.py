from copy import deepcopy

# class for puzzle game problem
class PuzzleGame:

    def __init__(self, grid=None):
        if grid is None:
            grid = []
        self.grid = grid

    def __eq__(self, other):
        return self.grid == other.grid

class PuzzleGameUtils:

    # misplaced tiles heuristic
    def heuristic_misplaced(state):
        grid = state.grid
        goal = [[1,2,3],[4,5,6],[7,8,-1]]
        misplaced = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] != goal[i][j]):
                    misplaced+=1

        return misplaced

    # manhattan distance heuristic
    def heuristic_manhattan(state):
        grid = state.grid
        goal = [[1,2,3],[4,5,6],[7,8,-1]]
        manhattan = 0

        for i in range(1,9):
            coord_grid = [(index, row.index(i)) for index, row in enumerate(grid) if i in row]
            coord_goal = [(index, row.index(i)) for index, row in enumerate(goal) if i in row]
            manhattan += abs(coord_goal[0][0] - coord_grid[0][0]) + abs(coord_goal[0][1] - coord_grid[0][1])

        return manhattan

    def successor_fn(state):
        grid = state.grid
        res = []
        #find coordinates where the -1 is
        coord = [(index, row.index(-1)) for index, row in enumerate(grid) if -1 in row]

        if (coord[0][0] + 1 < len(grid[0])):
            tmp = deepcopy(grid)
            row = coord[0][0]
            col = coord[0][1]
            tmp[row][col] = tmp[row + 1][col]
            tmp[row + 1][col] = -1
            res.append(("down", (PuzzleGame(tmp), 1)))

        if (coord[0][0] - 1 >= 0):
            tmp = deepcopy(grid)
            row = coord[0][0]
            col = coord[0][1]
            tmp[row][col] = tmp[row - 1][col]
            tmp[row - 1][col] = -1
            res.append(("up", (PuzzleGame(tmp), 1)))

        if (coord[0][1] + 1 < len(grid[0])):
            tmp = deepcopy(grid)
            row = coord[0][0]
            col = coord[0][1]
            tmp[row][col] = tmp[row][col + 1]
            tmp[row][col + 1] = -1
            res.append(("right", (PuzzleGame(tmp), 1)))

        if (coord[0][1] - 1 >= 0):
            tmp = deepcopy(grid)
            row = coord[0][0]
            col = coord[0][1]
            tmp[row][col] = tmp[row][col - 1]
            tmp[row][col - 1] = -1
            res.append(("left", (PuzzleGame(tmp), 1)))

        return res

    def step_cost(node, action):
        return 1




