from copy import deepcopy


class PuzzleGame:

    def __init__(self, grid=None):
        if grid is None:
            grid = []
        self.grid = grid


def heuristic_fn(state):
    grid = state.grid
    goal = [[1,2,3],[4,5,6],[7,8,-1]]
    misplaced = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if(grid[i][j] != goal[i][j]):
                misplaced+=1



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
        res.append(tmp)

    if (coord[0][0] - 1 >= 0):
        tmp = deepcopy(grid)
        row = coord[0][0]
        col = coord[0][1]
        tmp[row][col] = tmp[row - 1][col]
        tmp[row - 1][col] = -1
        res.append(tmp)

    if (coord[0][1] + 1 <= len(grid[0])):
        tmp = deepcopy(grid)
        row = coord[0][0]
        col = coord[0][1]
        tmp[row][col] = tmp[row][col + 1]
        tmp[row][col + 1] = -1
        res.append(tmp)

    if (coord[0][1] - 1 >= 0):
        tmp = deepcopy(grid)
        row = coord[0][0]
        col = coord[0][1]
        tmp[row][col] = tmp[row][col - 1]
        tmp[row][col - 1] = -1
        res.append(tmp)

    return res

def step_cost(node, action):
    return 1




