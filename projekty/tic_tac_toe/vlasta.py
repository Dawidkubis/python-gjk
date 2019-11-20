#Jupyter je lepsi
# ^-- ok
import numpy as np # podle me zbytecny jelikoz jsi stejne nepouzil vsechny moznosti numpy
                   # jako treba ten matrix rotation
                   # takhle je tvuj kod jenom dependent na jeste jedny veci, coz je
                   # zbytecny; musis si uvedomit ze kdybys tohle nekomu posilal,
                   # tak ten clovek musi mit nejenom python ale i numpy
ikonky = ["   "," X "," O "]
def render(board): # board jako argument - super
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

def compare3(a,b,c): # obecne vyjadreni, nice
    return a == b and b == c and a != 0

def check(board, move): # elegantni reseni, ale jde to i snadneji :D
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
        x = input("Zadejte tah od 0 do 8 \n > ") # eeh, input ve funkci - vedlejsi efekt
        OK = x.isnumeric() # nice, hezky reseni problemu vstupu
        if OK:
            OK = int(x) >= 0 and int(x) <= 8
            if OK:
                X = int(x)//3
                Y = int(x)%3
                OK = move((X, Y),1)

def move(move,player):
    global board # fuj fuj
    global lastMove # bleh
    OK = board[move] == 0 # chytry ze sis to zapsal do promenny
                          # diky tomu neprovadis stejny vypocet dvakrat
    if OK:
        board[move] = player
        lastMove = move
    return OK # vyuzivas return hodnot - nice
    
from random import randint
def AImove():
    #vim ze to neni minmax
    #^-- to ne no, ale je to zajimavy ozvlastneni programu
    while not move((randint(0,2),randint(0,2)), 2):
        continue
    return move
    

# LUKÁŠ - Tyhle module-level globaly by neměly fungovat, jsi si jistý, že jsi nahrál správný kód?
# hra
global board # wtf vlasto
board = np.zeros((3, 3), dtype=np.int)
global lastMove # wut; sice to nechazi chybu ale melo by
lastMove = (0,0)
player = 1
render(board)
while (not check(board, lastMove)[0]) and  check(board, lastMove)[1]:
    if player == 1:
        inputMove()
    else:
        AImove()
    render(board)
    player = (player%2)+1 # Hraje další hráč; 1 => 2; 2 => 1
                          # ^-- fajn ze komentujes
if check(board, lastMove)[0]:
    print("Vyhrál: "+ikonky[board[lastMove]])
else:
    print("Remíza")

# ma to divnou strukturu, na jednu stranu jsou nektery mista dobre napsany
# jiny jsou gay a pouzivaj globaly

# jinak + za to AI
