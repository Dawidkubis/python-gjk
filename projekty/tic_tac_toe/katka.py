plocha = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
hrac = "X"

def kontrola():
    if plocha[0][0] == plocha[0][1] and plocha[0][1] == plocha[0][2] and plocha[0][2] != " ":
        print("Vyhrál " + hrac)
        return True
    if plocha[1][0] == plocha[1][1] and plocha[1][1] == plocha[1][2] and plocha[1][2] != " ":
        print("Vyhrál " + hrac)
        return True
    if plocha[2][0] == plocha[2][1] and plocha[2][1] == plocha[2][2] and plocha[2][2] != " ":
        print("Vyhrál " + hrac)
        return True
    if plocha[0][0] == plocha[1][0] and plocha[1][0] == plocha[2][0] and plocha[2][0] != " ":
        print("Vyhrál " + hrac)
        return True
    if plocha[0][1] == plocha[1][1] and plocha[1][1] == plocha[2][1] and plocha[2][1] != " ":
        print("Vyhrál " + hrac)
        return True
    if plocha[0][2] == plocha[1][2] and plocha[1][2] == plocha[2][2] and plocha[2][2] != " ":
        print("Vyhrál " + hrac)
        return True
    if plocha[0][0] == plocha[1][1] and plocha[1][1] == plocha[2][2] and plocha[2][2] != " ":
        print("Vyhrál " + hrac)
        return True
    if plocha[0][2] == plocha[1][1] and plocha[1][1] == plocha[2][0] and plocha[2][0] != " ":
        print("Vyhrál " + hrac)
        return True
    return False

def vytiskni():
    print(plocha[0][0] + "|" + plocha[0][1] + "|" + plocha[0][2])
    print("-+-+-")
    print(plocha[1][0] + "|" + plocha[1][1] + "|" + plocha[1][2])
    print("-+-+-")
    print(plocha[2][0] + "|" + plocha[2][1] + "|" + plocha[2][2])

vytiskni()
while True:
    x = input()
    y = x.split()
    if plocha[int(y[0])][int(y[1])] == " ":
        plocha[int(y[0])][int(y[1])] = hrac
        if kontrola():
            vytiskni()
            break
        if hrac == "X":
            hrac = "O"
        else:
            hrac = "X"
    vytiskni()
