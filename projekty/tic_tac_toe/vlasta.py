#Jupyter je lepsi
import numpy as np
ikonky = ["   "," X "," O "]
def render(board):
    text = "+---+---+---+\n"
    for row in board:
        text += "|"
        for column in row:
            text += ikonky[column] + "|"
        text += "\n+---+---+---+\n"
    print(text)
    print("""+---+---+---+
| 0 | 1 | 2 |
+---+---+---+
| 3 | 4 | 5 |
+---+---+---+
| 6 | 7 | 8 |
+---+---+---+""")

def compare3(a,b,c):
    return a == b and b == c and a != 0

def check(board, move):
    #print(board, move)
    end = False
    #kontrola řádku
    end = end or compare3(board[0, move[1]],board[1, move[1]],board[2, move[1]])
    #kontrola sloupce
    end = end or compare3(board[move[0], 0],board[move[0], 1],board[move[0], 2])
    #kontrola diagnálně
    end = end or compare3(board[0, 0],board[1, 1],board[2, 2])
    end = end or compare3(board[0, 2],board[1, 1],board[2, 0])
    
    return (end, 0 in board)
    
def inputMove():
    x = ""
    OK = False
    while not OK:
        x = input("Zadejte tah od 0 do 8 \n > ")
        OK = x.isnumeric()
        if OK:
            OK = int(x) >= 0 and int(x) <= 8
            if OK:
                X = int(x)//3
                Y = int(x)%3
                OK = move((X, Y),1)

def move(move,player):
    global board
    global lastMove
    OK = board[move] == 0
    if OK:
        board[move] = player
        lastMove = move
    return OK
    
from random import randint
def AImove():
    #vim ze to neni minmax
    while not move((randint(0,2),randint(0,2)), 2):
        continue
    return move
    
    
#hra
global board
board = np.zeros((3, 3), dtype=np.int)
global lastMove
lastMove = (0,0)
player = 1
render(board)
while (not check(board, lastMove)[0]) and  check(board, lastMove)[1]:
    if player == 1:
        inputMove()
    else:
        AImove()
    render(board)
    player = (player%2)+1 #Hraje další hráč; 1 => 2; 2 => 1
if check(board, lastMove)[0]:
    print("Vyhrál: "+ikonky[board[lastMove]])
else:
    print("Remíza")
    
