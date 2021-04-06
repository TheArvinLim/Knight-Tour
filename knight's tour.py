import numpy as np
from copy import copy
from warnings import warn
from numpy.linalg import norm   
import random

# this function is complete
def knights_tour(starting_pos):
    board = np.zeros((8,8))
    board[starting_pos[0],starting_pos[1]] = 1
    current_pos = starting_pos
    move_tree = Tree(current_pos)

    while not check_solved(board):
        possible_moves = get_moves(current_pos, board)
        for move in possible_moves:
            current_move = move_tree.add_child(move)
        
        current_pos = current_move.data
        board[current_pos[0], current_pos[1]] = 1
        

    print("solved")

def get_moves(current_pos, board):
    v = [-1, -2, -2, -1, 1, 2, 2, 1]
    h = [-2, -1, 1, 2, 2, 1, -1, -2]
    possible_moves = []

    for i in range(0,8):
        move = np.add(current_pos, [v[i], h[i]])
        if not (move[0] < 0 or move[0] > 7 or move[1] < 0 or move[1] > 7 or board[move[0], move[1]]):
            possible_moves.append(move)

    return possible_moves

def check_solved(board):
    for i in range(0,8):
        for j in range(0,8):
            if not board[i,j]:
                return False
    return True

class Tree(object):
    def __init__(self, data, children=None, parent=None):
        self.data = data
        self.children = children or []
        self.parent = parent

    def add_child(self, data):
        new_child = Tree(data, parent=self)
        self.children.append(new_child)
        return new_child

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return not self.children

    def __str__(self):
        if self.is_leaf():
            return str(self.data)
        return '{data} [{children}]'.format(data=self.data, children=', '.join(map(str, self.children)))

knights_tour([0,0])

