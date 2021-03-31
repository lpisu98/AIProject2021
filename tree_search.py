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

class SearchStrategies:


    def breadthFirstSearch(problem):
        fringe = []
        expanded_nodes = 1
        total_nodes = 1
        fringe.append(Node(problem.initial_state))

        while 1:
            if(len(fringe) == 0):
                return -1

            node = fringe.pop(0)
            if(problem.goal_test(node) == True):
                print("Expanded nodes:", expanded_nodes)
                print("Total nodes:", total_nodes)
                return node

            expanded_nodes+=1
            for n in expand(node, problem):
                total_nodes += 1
                fringe.append(n)

    def depthFirstSearch(problem):
        fringe = []
        expanded_nodes = 1
        total_nodes = 1
        fringe.append(Node(problem.initial_state))

        while 1:
            if(len(fringe) == 0):
                return -1

            node = fringe.pop() #gives us the last element
            if(problem.goal_test(node) == True):
                print("Expanded nodes:",expanded_nodes)
                print("Total nodes:", total_nodes)
                return node

            # depth limit 4400
            if(node.depth < 4400):
                new_nodes = expand(node, problem)
                expanded_nodes += 1
                if(new_nodes == []):
                    # if the expanded node has no children we can check if we can delete some parent nodes
                    for i in range(node.depth):
                        delete = True
                        for n in fringe:
                            if node == n.parent_node:
                                delete = False
                                break

                        if delete == True:
                            tmp = node.parent_node
                            tmp.children_nodes.remove(node)
                            total_nodes -= 1
                            node = tmp

                for n in new_nodes:
                    if (n != node.parent_node):
                        total_nodes += 1
                        fringe.append(n)
                    # else : discard
            else:
                # for every node in a path we check if the node has no children in the fringe and we delete it
                for i in range(node.depth):
                    delete = True
                    for n in fringe:
                        if node == n.parent_node:
                            delete = False
                            break

                    if delete == True:
                        tmp = node.parent_node
                        tmp.children_nodes.remove(node)
                        total_nodes -= 1
                        node = tmp
                    else:
                        break


    def aStarSearch(problem):
        fringe = []
        expanded_nodes = 1
        total_nodes = 1
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
                print("Expanded nodes:", expanded_nodes)
                print("Total nodes:", total_nodes)
                return node
            expanded_nodes+=1
            for n in expand(node, problem):
                total_nodes += 1
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

'''
def expand(node, problem):
    successors = []
    skip = False
    for (action, result) in problem.successor_fn(node.state):
        actual = node
        for i in range(node.depth):
            actual = actual.parent_node
            if (actual != None and result[0] == actual.state):
                skip = True  # skip this iteration so that we don't add repeated states
                break

        if (not skip):
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

    return successors
'''
