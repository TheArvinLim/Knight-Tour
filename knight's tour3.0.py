import numpy as np
from copy import copy
from warnings import warn
from numpy.linalg import norm   
import random
import time

def knights_tour(starting_pos):
    current_move = Tree(starting_pos)
    board = np.zeros((6,6))
    board[current_move.data[0],current_move.data[1]] = 1

    while not check_solved(board):
        if current_move.children:
            current_move = current_move.children[0]
            board[current_move.data[0],current_move.data[1]] = 1

        elif not current_move.explored:
            current_move.explored = True
            possible_moves = get_moves(current_move.data, board)    

            if possible_moves:
                for move in possible_moves:    
                    current_move.add_child(move)

        elif current_move.is_root():
            break

        else:
            board[current_move.data[0],current_move.data[1]] = 0
            current_move.remove_self()
            current_move = current_move.parent
            board[current_move.data[0],current_move.data[1]] = 1

    if check_solved(board):
        print("Solution Found")
        move_history = get_move_history(current_move)
        for i in reversed(move_history):
            print(str(i))

    else:
        print("No solution")

def check_solvable(board, current_position):
    for i in range(0,board.shape[0]):
        for j in range(0,board.shape[1]):
            if not board[i,j]:
                visitable = False
                possible_moves = get_moves([i,j], board)
                for move in possible_moves:
                    if board[move[0],move[1]] == 0 or (move[0] == current_position[0] and move[1] == current_position[1]):
                        visitable = True
                        break
                if not visitable:
                    return False
    return True

def get_moves(position, board):
    v = [-1, -2, -2, -1, 1, 2, 2, 1]
    h = [-2, -1, 1, 2, 2, 1, -1, -2]
    possible_moves = []

    for i in range(0,8):
        move = np.add(position, [v[i], h[i]])
        if not (move[0] < 0 or move[0] >= board.shape[0] or move[1] < 0 or move[1] >= board.shape[1] or board[move[0],move[1]]):
            possible_moves.append(move)

    return possible_moves


def get_move_history(current_move):
    move_history = [np.array(current_move.data)]
    while not current_move.is_root():
        current_move = current_move.parent
        move_history.append(np.array(current_move.data))

    return move_history

def check_solved(board):
    for i in range(0,board.shape[0]):
        for j in range(0,board.shape[1]):
            if not board[i,j]:
                return False
    return True

class Tree(object):
    def __init__(self, data, children=None, parent=None):
        self.data = data
        self.children = children or []
        self.parent = parent
        self.explored = False

    def add_child(self, data):
        new_child = Tree(data, parent=self)
        self.children.append(new_child)
        return new_child

    def remove_self(self):
        self.parent.children.remove(self)

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return not self.children

    def __str__(self):
        if self.is_leaf():
            return str(self.data)
        return '{data} [{children}]'.format(data=self.data, children=', '.join(map(str, self.children)))


start_time = time.time()
knights_tour([0,0])
print("--- %s seconds ---" % (time.time() - start_time))