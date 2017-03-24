"""
	AI Assignment 1
	Author: Ben Russell
	Date:1/14/2017
"""
"""
	Main class
"""
import sys
import Node
import PQ

size = 4
goal_state1 = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F',' ']
goal_state2 = ['1','2','3','4','5','6','7','8','9','A','B','C','D','F','E',' ']

def move_right(blank_index, new_puzzle):
    if blank_index + 1 < new_puzzle.__len__():
        a = new_puzzle[blank_index + 1]
        new_puzzle.remove(a)
        new_puzzle.insert(blank_index, a)
        return new_puzzle
    else:
        return -1

def move_down(blank_index, new_puzzle):
    if blank_index + size < new_puzzle.__len__():
        a = new_puzzle[blank_index + size]
        b = new_puzzle[blank_index]
        new_puzzle.remove(a)
        new_puzzle.remove(b)
        new_puzzle.insert(blank_index, a)
        new_puzzle.insert(blank_index + size, b)
        return new_puzzle
    else:
        return -1

def move_left(blank_index, new_puzzle):
    if blank_index - 1 >= 0:
        a = new_puzzle[blank_index - 1]
        b = new_puzzle[blank_index]
        new_puzzle.remove(a)
        new_puzzle.remove(b)
        new_puzzle.insert(blank_index - 1, b)
        new_puzzle.insert(blank_index, a)

        return new_puzzle
    else:
        return -1

def move_up(blank_index, new_puzzle):
    if blank_index - size >= 0:
        a = new_puzzle[blank_index - size]
        b = new_puzzle[blank_index]
        new_puzzle.remove(b)
        new_puzzle.remove(a)
        new_puzzle.insert(blank_index - size, b)
        new_puzzle.insert(blank_index, a)
        return new_puzzle
    else:
        return -1

def not_visited(state, visited_list):
    not_vis = True
    for i in range (0, visited_list.__len__(), 1):
        if str(visited_list[i]) == str(state):
            not_vis = False
    return not_vis

def move(puzzle):
    blank_index = puzzle.index(' ')
    state_list = []
    size2 = size * size
    #move right
    if blank_index % size < 3:
        puzzle2 = puzzle[:]
        new_puzzle = move_right(blank_index, puzzle2)
        if new_puzzle is not -1:
            state_list.append(new_puzzle)

    #move down
    if blank_index % size2 < 12:
        puzzle2 = puzzle[:]
        new_puzzle = move_down(blank_index, puzzle2)
        if new_puzzle is not -1:
            state_list.append(new_puzzle)

    #move left
    if blank_index % size > 0:
        puzzle2 = puzzle[:]
        new_puzzle = move_left(blank_index, puzzle2)
        if new_puzzle is not -1:
            state_list.append(new_puzzle)

    #move up
    if blank_index % size2 > 3:
        puzzle2 = puzzle[:]
        new_puzzle = move_up(blank_index, puzzle2)
        if new_puzzle is not -1:
            state_list.append(new_puzzle)

    return state_list
'''
    BFS search algorithm
'''
def bfs(state):
    queue = []
    visited_list = [state]
    node = Node.Node(state, 0)
    queue.append(node)
    num_expanded = 0
    max_fringe = 0
    num_created = 1

    while queue:
        node = queue.pop(0)
        depth = node.depth
        num_expanded += 1
        if str(node.state) == str(goal_state1) or str(node.state) == str(goal_state2):
            print("{}, {}, {}, {}".format(depth, num_created, num_expanded, max_fringe))
            return depth

        states = move(node.state)
        for s in states:
            if not_visited(s, visited_list):
                queue.append(Node.Node(s, depth + 1))
                num_created += 1
                visited_list.append(s)

        if max_fringe < visited_list.__len__() - num_expanded:
            max_fringe = visited_list.__len__() - num_expanded
    return
'''
    DFS search algorithm
'''
def dfs(state, option):

    stack = []
    visited_list = [state]
    node = Node.Node(state, 0)
    max_fringe = 1
    num_expanded = 0
    num_created = 1
    stack.insert(0, node)
    while stack:
        node = stack.pop(0)
        depth = node.depth
        num_expanded += 1
        if str(node.state) == str(goal_state1) or str(node.state) == str(goal_state2):
            print("{}, {}, {}, {}".format(depth, num_created, num_expanded, max_fringe))
            return

        if option is not None:
            counter = 0
            while node.depth > int(option):
                counter += 1
                if str(node.state) == str(goal_state1) or str(node.state) == str(goal_state2):
                    print("{}, {}, {}, {}".format(depth, num_created, num_expanded, max_fringe))
                    return
                if max_fringe - counter < 0:
                    print "Goal not found"
                    return -1
                stack.append(node)
                node = stack.pop(0)
                depth = node.depth

        states = move(node.state)
        for s in reversed(states):
            if not_visited(s, visited_list):
                stack.insert(0, Node.Node(s, depth + 1))
                num_created += 1
                visited_list.append(s)
        if max_fringe < visited_list.__len__() - num_expanded:
            max_fringe = visited_list.__len__() - num_expanded
    return
'''
    GBFS search algorithm
'''
def gbfs(state, option):
    visited_list = [state]
    node = Node.Node(state, 0)
    queue = PQ.PQ()
    queue.push(node, check_distance(state, option))
    num_expanded = 0
    max_fringe = 0
    num_created = 1

    while queue:
        node = queue.pop()
        depth = node.depth
        num_expanded += 1
        if str(node.state) == str(goal_state1) or str(node.state) == str(goal_state2):
            print("{}, {}, {}, {}".format(depth, num_created, num_expanded, max_fringe))
            return depth

        states = move(node.state)
        for s in states:
            if not_visited(s, visited_list):
                priority = check_distance(s, option)
                queue.push(Node.Node(s, depth + 1), priority)
                num_created += 1
                visited_list.append(s)

        if max_fringe < visited_list.__len__() - num_expanded:
            max_fringe = visited_list.__len__() - num_expanded
    return
'''
    ASTAR search algorithm
'''
def a_star(state, option):
    visited_list = [state]
    node = Node.Node(state, 0)
    num_expanded = 0
    max_fringe = 0
    num_created = 1
    queue = PQ.PQ()
    queue.push(node, check_distance(state, option) + num_created)
    while queue:
        node = queue.pop()
        depth = node.depth
        num_expanded += 1
        if str(node.state) == str(goal_state1) or str(node.state) == str(goal_state2):
            print("{}, {}, {}, {}".format(depth, num_created, num_expanded, max_fringe))
            return depth

        states = move(node.state)
        for s in states:
            if not_visited(s, visited_list):
                priority = check_distance(s, option) + num_created
                queue.push(Node.Node(s, depth + 1), priority)
                num_created += 1
                visited_list.append(s)

        if max_fringe < visited_list.__len__() - num_expanded:
            max_fringe = visited_list.__len__() - num_expanded
    return
def check_distance(state, heuristic):
    gs1 = goal_state1
    gs2 = goal_state2
    count1 = 0
    count2 = 0
    if heuristic == 'h1':
        for i in range(len(state)):
            if gs1[i] is not state[i]:
                count1 +=1
        for i in range(len(state)):
            if gs2[i] is not state[i]:
                count2 +=1
    elif heuristic == 'h2':
        for i in range(len(state)):
            count1 += (gs1.index(state[i]) - i).__abs__()
        for i in range(len(state)):
            count2 += (gs2.index(state[i]) - i).__abs__()

    count = min(count1, count2)
    return count

def select_search(search, state, option):
    if search == 'BFS':
        return bfs(state)
    elif search == 'DFS':
        return dfs(state, None)
    elif search == 'DLS':
        return dfs(state, option)
    elif search == 'GBFS':
        return gbfs(state, option)
    elif search == 'Astar':
        return a_star(state, option)

def main():

    args = sys.argv[1:]
    if not args:
        print 'no args!'
        exit(1)
    initial_state = list(args[0])
    search_method = args[1]
    if args.__len__() == 3:
        option = args[2]
    else:
        option = None
    print initial_state
    print search_method
    print option
    """
    #************* Debug
    initial_state = ['1','2','3','4','5','6','7','8','9','A','B','C',' ','D', 'F','E']
    #initial_state = [1,2,3,4,5,6,7,8,9,'A','B','C',' ','D', 'F','E']
    #initial_state = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', ' ', 'E', 'D', 'F', 'C', 'B']
    #initial_state = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'F', 'B', 'D', 'E', ' ', 'C']
    #initial_state = [' ',1,2,3]
    search_method = "DLS"
    option = '1'
    #************* End Debug
    """
    select_search(search_method, initial_state, option)

if __name__ == '__main__':
    main()

