"""
Tic Tac Toe Player
"""

import math
import random

X = "X"
O = "O"
EMPTY ="_"


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x=0;
    y=0;
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]== "X":
                x+=1
            elif board[i][j]=="O":
                y+=1

    if x==y:
        return X
    else:
        return O




def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    s=[]
    for i in range(len(board)):
        for j in range (len(board[i])):
            if board[i][j]=="_":
                s.append((i,j))
    return  s




def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    board[action[0]][action[1]]=player(board)
    return  board



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(len(board)):
       c1=0
       c2=0
       for j in range(len(board[i])):
           if board[i][j]=="X":
                c1+= 1
                if c1 == 3:
                   return X
                   break
           elif board[i][j]=="O":
               c2 += 1
               if c2 == 3:
                   return O
                   break

    c1=0
    c2=0
    c3=0
    c4=0
    c5=0
    c6=0

    for j in board:
        if j[0] =="X":
            c1 += 1
            if c1 == 3:
                return X
                break
    for j in board:
        if j[1] =="X" :
            c2 += 1
            if c2 == 3:
                return X
                break

    for j in board:
        if j[2] == "X":
            c3 += 1
            if c3 == 3:
                return X
                break
    for j in board:
        if j[0] == "O":
            c4+= 1
            if c4 == 3:
                return O
                break
    for j in board:
        if j[1] == "O":
            c5+= 1
            if c5 == 3:
                return O
                break

    for j in board:
        if j[2] == "O":
            c6+= 1
            if c6 == 3:
                return O
                break
    count31=0
    count32=0
    for i in range(len(board)):
        if board[i][i]=="X":
            count31+=1
            if count31 ==3:
                return board[i][i]
        elif  board[i][i]=="O":
            count32+=1
            if count32==3:
                return board[i][i]
    count41=0
    count42=0
    for i in range(len(board)):
        c=len(board)-i-1

        if board[i][c]=="X" :
            count41+=1
            if count41==3:
                return board[i][c]
        elif board[i][c]=="O":
            count42+=1
            if count42==3:
                return board[i][c]


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return len(actions(board))==0 or winner(board) is not None




def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
        return 1
    elif winner(board)==O:
        return -1
    else:
        return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    possible_actions = actions(board)

    if len(possible_actions) == 9:
        return random.choice(possible_actions)

    current_player = player(board)

    opt_action = help(board, current_player)

    return opt_action[1]


def help(board, current_player):
    """
    Implements the Minimax for both X and O
    """
    if terminal(board):
        return utility(board), None

    else:

        all_actions = actions(board)
        val = 1.0
        action = []

        if current_player == X:
            val = -1.0

            for i in all_actions:
                temp = board.copy()
                temp = result(temp, i)
                ans = help(temp, O)
                temp_val = val
                val = max(val, ans[0])
                if val > temp_val:
                    action = i
                board[i[0]][i[1]] = EMPTY
                if val == 1:
                    break

        else:


            for i in all_actions:
                temp = board.copy()
                temp = result(temp, i)
                ans = help(temp, X)
                temp_val = val
                val = min(val, ans[0])
                if val < temp_val:
                    action = i
                board[i[0]][i[1]] = EMPTY
                if val == -1:
                    break

        return val, action