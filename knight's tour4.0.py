import numpy as np
from copy import copy
from warnings import warn
from numpy.linalg import norm   
import random
import time
from lab6_functions import*



def generate_graph(a,b):
    board = Network()
    for i in range(0,a):
        for j in range(0,b):
            id_number = (i*a) + j
            board.add_node(id_number, False)

    for i in range(0,a):
        for j in range(0,b):
            legal_moves = get_moves([i, j], a, b)
            from_id = (i*a) + j
            from_nd = board.get_node(from_id)
            for moves in legal_moves:
                to_id = (moves[0]*a) + moves[1]
                to_nd = board.get_node(to_id)
                board.join_nodes(from_nd,to_nd,1)

    return board

def onward_moves(node):
    onward_moves = 0
    for arc in node.arcs_out:
        to_node = arc.to_node
        if to_node.value == False:
            onward_moves = onward_moves + 1
    
    return onward_moves


def knights_tour(n,path,u,limit):
    path.append(u)
    u.value = True
    if n < limit:
        neighbours = []
        for arc in u.arcs_out:
            neighbours.append(arc.to_node)

        solved = False

        # num_onward_moves = []

        # for neighbour in neighbours:
        #     num_onward_moves.append(onward_moves(neighbour))

        for neighbour in neighbours:
            if neighbour.value == False:
                solved = knights_tour(n+1, path, neighbour, limit)
            if solved:
                break

        if not solved:
            path.pop()
            u.value = False
            
    else:
        solved = True
    
    return solved

def get_moves(position, a, b):
    v = [-1, -2, -2, -1, 1, 2, 2, 1]
    h = [-2, -1, 1, 2, 2, 1, -1, -2]
    possible_moves = []

    for i in range(0,8):
        move = np.add(position, [v[i], h[i]])
        if not (move[0] < 0 or move[0] >= a or move[1] < 0 or move[1] >= b):
            possible_moves.append(move)

    return possible_moves

board_size = [7, 7]


board = generate_graph(board_size[0],board_size[1])
start_time = time.time()
path = []
knights_tour(0,path,board.get_node(0),(board_size[0]*board_size[1]-1))
print("--- %s seconds ---" % (time.time() - start_time))

for node in path:
    id_number = node.name
    row = int(id_number/board_size[0])
    col = id_number - row*board_size[1]
    print(str([row, col]))
