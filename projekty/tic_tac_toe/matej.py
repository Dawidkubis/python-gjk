grid = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

x = False
# nazev promenny nic nerika
# taky ta definice je kilometry od mista kde se
# ta promenna pouzije :(

def play1(): # dve oddeleny funkce pro ruzne hrace
             # debilni protoze a) nemuzeme snadno pridat hrace
             #                 b) opakovani kodu

    global x_input_1
    global y_input_1
    # oof, globaly
    
    true_x = False # lol, to jsou nazvy.
    true_y = False # procs tam nenapsal rovnou:
    #false_y = True
    # :D
    # ale vazne by bylo lepsi:
    #bool_y = False
    true_taken_1 = False

    print("Now will play player 1") # english

    while not true_taken_1: # celkem elegantni, az na to ze moc ne
        # chytrejsi 

        while not true_x:

            x_input_1 = int(input("Enter x axis position (1, 2, 3): "))

            if x_input_1 == 1:
                true_x = True
            elif x_input_1 == 2:
                true_x = True
            elif x_input_1 == 3:
                true_x = True
            else:
                print("Try again (1, 2, 3)")

        while not true_y:

            y_input_1 = int(input("Enter y axis position (1, 2, 3): "))

            if y_input_1 == 1:
                true_y = True
            elif y_input_1 == 2:
                true_y = True
            elif y_input_1 == 3:
                true_y = True
            else:
                print("Try again (1, 2, 3)")

        if grid[x_input_1 - 1][y_input_1 - 1] not in ("X", "O"):
            true_taken_1 = True

        else:
            print("That position is taken")
            true_x = False
            true_y = False

    grid[x_input_1 - 1][y_input_1 - 1] = "X"

    print(grid[0][0] + "  |  " + grid[1][0] + "  |  " + grid[2][0] + "\n" + "__" + "   " + "__" + "   " + "__" +
          "\n" + grid[0][1] + "   |  " + grid[1][1] + "  |  " + grid[2][1] + "\n" + "__" + "   " + "__" + "   " + "__" +
          "\n" + grid[0][2] + "   |  " + grid[1][2] + "  |  " + grid[2][2]) # celkem v pohode lol

def play2():
    print("Now will play player 2\n")
    global x_input_2
    global y_input_2
    # globaly fuj fuj
    true_taken_2 = False
    true_x_1 = False
    true_y_1 = False

    while not true_taken_2:

        while not true_x_1:

            x_input_2 = int(input("Enter x axis position (1, 2, 3): "))

            if x_input_2 == 1:
                true_x_1 = True
            elif x_input_2 == 2:
                true_x_1 = True
            elif x_input_2 == 3:
                true_x_1 = True
            else:
                print("Try again (1, 2, 3)")

        while not true_y_1:
            y_input_2 = int(input("Enter y axis position (1, 2, 3): "))

            if y_input_2 == 1:
                true_y_1 = True
            elif y_input_2 == 2:
                true_y_1 = True
            elif y_input_2 == 3:
                true_y_1 = True
            else:
                print("Try again (1, 2, 3)")

        if grid[x_input_2 - 1][y_input_2 - 1] not in ("X", "O"):
            true_taken_2 = True

        else:
            print("That position is taken")
            true_x_1 = False
            true_y_1 = False

    grid[x_input_2 - 1][y_input_2 - 1] = "O"

    print(grid[0][0] + "  |  " + grid[1][0] + "  |  " + grid[2][0] + "\n" + "__" + "   " + "__" + "   " + "__" +
          "\n" + grid[0][1] + "   |  " + grid[1][1] + "  |  " + grid[2][1] + "\n" + "__" + "   " + "__" + "   " + "__" +
          "\n" + grid[0][2] + "   |  " + grid[1][2] + "  |  " + grid[2][2])

def win():
    global x
    # globaly fuj fuj
    x0_y0 = grid[0][0] # <-- gay
    x0_y1 = grid[0][1]
    x0_y2 = grid[0][2]
    x1_y0 = grid[1][0]
    x1_y1 = grid[1][1]
    x1_y2 = grid[1][2]
    x2_y0 = grid[2][0]
    x2_y1 = grid[2][1]
    x2_y2 = grid[2][2]

    if x0_y0 == x0_y1 == x0_y2 and x0_y0 == "X":
        print("Player 1 wins")
        x = True

    elif x1_y0 == x1_y1 == x1_y2 and x1_y0 == "X":
        print("Player 1 wins")
        x = True
    elif x2_y0 == x2_y1 == x2_y2 and x2_y0 == "X":
        print("Player 1 wins")
        x = True
    elif x0_y0 == x1_y0 == x2_y0 and x0_y0 == "X":
        print("Player 1 wins")
        x = True
    elif x0_y1 == x1_y1 == x0_y2 and x0_y1 == "X":
        print("Player 1 wins")
        x = True
    elif x0_y2 == x1_y2 == x2_y2 and x0_y2 == "X":
        print("Player 1 wins")
        x = True
    elif x0_y0 == x1_y1 == x2_y2 and x0_y0 == "X":
        print("Player 1 wins")
        x = True
    elif x2_y0 == x1_y1 == x0_y2 and x2_y0 == "X":
        print("Player 1 wins")
        x = True

    elif x0_y0 == x0_y1 == x0_y2 and x0_y0 == "O":
        print("Player 2 wins")
        x = True
    elif x1_y0 == x1_y1 == x1_y2 and x1_y0 == "O":
        print("Player 2 wins")
        x = True
    elif x2_y0 == x2_y1 == x2_y2 and x2_y0 == "O":
        print("Player 2 wins")
        x = True
    elif x0_y0 == x1_y0 == x2_y0 and x0_y0 == "O":
        print("Player 2 wins")
        x = True
    elif x0_y1 == x1_y1 == x0_y2 and x0_y1 == "O":
        print("Player 2 wins")
        x = True
    elif x0_y2 == x1_y2 == x2_y2 and x0_y2 == "O":
        print("Player 2 wins")
        x = True
    elif x0_y0 == x1_y1 == x2_y2 and x0_y0 == "O":
        print("Player 2 wins")
        x = True
    elif x2_y0 == x1_y1 == x0_y2 and x2_y0 == "O":
        print("Player 2 wins")
        x = True

while not x:
    win()
    play1()

    win()
    if not x:
        play2()

print("End of the game")
