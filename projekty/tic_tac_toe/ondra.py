board = ["[ ]", "[ ]", "[ ]",
         "[ ]", "[ ]", "[ ]",
         "[ ]", "[ ]", "[ ]"]
player_2 = False
Hra = True
kolo = 1
winner_2 = None

#spuští funkce ve správném pořadí
def tah():
    Tah = Input_pos()
    while Input_chack(Tah) == False:
        Tah = Input_pos()
    Move(Tah)
    Show()

#zobarí hrací desku
def Show():
    print(board[0], board[1], board[2], sep="")
    print(board[3], board[4], board[5], sep="")
    print(board[6], board[7], board[8], sep="")
    print("_________")

#vrátí array s xy informací o tahu
def Input_pos():
    player = int(player_2) + 1
    print("hráč", player, "hraje")
    vert = int(input("zadej sloupec (max 3)"))
    while vert > 3:
        print("vstup nesmí být větší než 3")
        vert = int(input("zadej sloupec (max 3)"))
    hor = int(input("zadej řádek (max 3)"))
    while hor > 3:
        hor = int(input("zadej řádek (max 3)"))
        print("vstup nesmí být větší než 3")
    tah = [vert, hor]
    return To_Index(tah)

#změní políčko
def Move(tah):
    if Input_chack(tah):
        if player_2:
            x = "O"
        else:
            x = "X"
        board[tah] = "[" + x + "]"
    else:
        pass

#skontroluje platnost vstupu
def Input_chack(index):
    if not board[index] == "[ ]":
        print("pole je již obsazené")
        return False
    else:
        return True

#převede array s xy pozicí do indexu
def To_Index(tah):
    index = tah[0] + ((tah[1] - 1) * 3) - 1
    return index

#skontroluje zde hráč nevyhrál
def Chack():
    if board[0] == board[1] and board[0] == board[2] and not board[0] == "[ ]": #123
        if board[0] == "[X]":
            return True
        else:
            return False
    elif board[3] == board[4] and board[3] == board[5] and not board[3] == "[ ]": #456
        if board[3] == "[X]":
            return True
        else:
            return False
    elif board[6] == board[7] and board[6] == board[8] and not board[6] == "[ ]": #789
        if board[6] == "[X]":
            return True
        else:
            return False
    elif board[0] == board[3] and board[0] == board[6] and not board[0] == "[ ]": #147
        if board[0] == "[X]":
            return True
        else:
            return False
    elif board[1] == board[4] and board[1] == board[7] and not board[1] == "[ ]": #258
        if board[1] == "[X]":
            return True
        else:
            return False
    elif board[2] == board[5] and board[2] == board[8] and not board[2] == "[ ]": #369
        if board[2] == "[X]":
            return True
        else:
            return False
    elif board[0] == board[4] and board[0] == board[8] and not board[0] == "[ ]": #159
        if board[0] == "[X]":
            return True
        else:
            return False
    elif board[2] == board[4] and board[2] == board[6] and not board[2] == "[ ]": #357
        if board[2] == "[X]":
            return True
        else:
            return False
    else:
        return None

Show()
while Hra:
    tah()
    if not Chack() == None:
        Hra = False
        if player_2:
            print("Hráč 2 wyhrál v kole", kolo)
        else:
            print("Hráč 1 wyhrál v kole", kolo)
    player_2 = not player_2
    kolo += 1
    if kolo > 8:
        Hra = False
        print("Hra skončila bez výsledku")
