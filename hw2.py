import numpy as np
import random

def create_board():
    return np.zeros((3,3))

def place(board, player, position):
    x = position[0]
    y = position[1]
    board[x,y] = player

def possibilities(board):
    temp = np.where(board == 0)
    res = []
    for each in range(len(temp[0])):
        res.append((temp[0][each],temp[1][each]))
    return res
    
def random_place(board, player):
    pos = random.choice(possibilities(board))
    place(board,player,pos)

def row_win(board, player):
    if player == 1:
        if np.array_equal(board[0,:],[1,1,1]):
            return True
        if np.array_equal(board[1,:],[1,1,1]):
            return True
        if np.array_equal(board[2,:],[1,1,1]):
            return True
    elif player == 2:
        if np.array_equal(board[0,:],[2,2,2]):
            return True
        if np.array_equal(board[1,:],[2,2,2]):
            return True
        if np.array_equal(board[2,:],[2,2,2]):
            return True
    else:
        return False 
    
def col_win(board, player):
    if player == 1:
        if np.array_equal(board[:,0],[1,1,1]):
            return True
        if np.array_equal(board[:,1],[1,1,1]):
            return True
        if np.array_equal(board[:,2],[1,1,1]):
            return True
    elif player == 2:
        if np.array_equal(board[:,0],[2,2,2]):
            return True
        if np.array_equal(board[:,1],[2,2,2]):
            return True
        if np.array_equal(board[:,2],[2,2,2]):
            return True
    else:
        return False 

def diag_win(board, player):
    if player == 1:
        if np.array_equal(np.diagonal(board),[1,1,1]):
            return True
        if np.array_equal(np.diag(np.fliplr(board)),[1,1,1]):
            return True
    elif player == 2:
        if np.array_equal(np.diagonal(board),[2,2,2]):
            return True
        if np.array_equal(np.diag(np.fliplr(board)),[2,2,2]):
            return True
    else:
        return False 

def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if col_win(board, player) or row_win(board, player) or diag_win(board, player):
            return player
    if np.all(board != 0):
        winner = -1
    return winner
    
def play_game():
    board = create_board()
    for player in [1,2,1,2,1,2,1,2,1]:
        random_place(board, player)
        if evaluate(board) != 0:
            return evaluate(board)

def play_strategic_game():
    board, winner = create_board(), 0
    board[1,1] = 1
    while winner == 0:
        for player in [2,1]:
            random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                break
    return winner

import time
import matplotlib.pyplot as plt

start_time = time.time() 
winners = []
for x in range(1000):
    winners.append( play_game() )
end_time = time.time()
diff_time = end_time - start_time
print(diff_time)
plt.hist(winners) 
plt.show()
    
start_time = time.time() 
winners = []
for x in range(1000):
    winners.append( play_strategic_game() )
end_time = time.time()
diff_time = end_time - start_time
print(diff_time)
plt.hist(winners) 
plt.show()