plocha = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]] # globalni promenne;
hrac = "X"                                                   # spatnej zvyk

def kontrola(): # kontrola vsech moznosti; celkem v pohode tady ale slo to vyresit chytreji
                # kdybychom najednou zmenili plochu z 3x3 na 4x4 tak uz by to nefungovalo
                # jinak je to celkem hezky
    if plocha[0][0] == plocha[0][1] and plocha[0][1] == plocha[0][2] and plocha[0][2] != " ":
        print("Vyhrál " + hrac) # print ve funkci, ne moc idealni z funkcionalniho hlediska
        # protoze `hrac` je tady globalni promenna; nevadi, to jeste budeme resit; v takhle
        # malym programu to ani tolik nevadi
        return True
    if plocha[1][0] == plocha[1][1] and plocha[1][1] == plocha[1][2] and plocha[1][2] != " ":
        print("Vyhrál " + hrac)
        return True # skvele ze je tady return, diky tomuhle se utece z funkce aniz by se kontroloval zbytek
    if plocha[2][0] == plocha[2][1] and plocha[2][1] == plocha[2][2] and plocha[2][2] != " ":
        #if plocha[2][0] == plocha[2][1] == plocha[2][2] != " ":
        # ^ ekvivalence, asi trochu hezci
        # je to ale specifikum pythonu ze to funguje
        # takze tohle je ve skutecnosti v poradku
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

def vytiskni(): # tady vsechno super
    print(plocha[0][0] + "|" + plocha[0][1] + "|" + plocha[0][2])
    print("-+-+-")
    print(plocha[1][0] + "|" + plocha[1][1] + "|" + plocha[1][2])
    print("-+-+-")
    print(plocha[2][0] + "|" + plocha[2][1] + "|" + plocha[2][2])

vytiskni()
while True:
    x = input()
    y = x.split() # asi bych tohle zkratil, ta promenna x tam tak trochu visi bez cile
                  # taky by mozna bylo chytry si rovnou vzit prvni 2 prvky z `x.split()`
    # napsal bych:
    #x = input()
    #x = x.split()
    # nebo:
    #x = input().split()
    # k tomu ze bych rovnou vzal 2 prvky tak bych napsal:
    #x = input().split()
    #y = int(x[0])
    #x = int(x[1])
    if plocha[int(y[0])][int(y[1])] == " ": # tady by bylo: `plocha[y][x] == " "`
        plocha[int(y[0])][int(y[1])] = hrac
        if kontrola(): # tohle se mi libi - hromada lidi by napsala:
                       # `if kontrola() == True:`
            vytiskni()
            break
        if hrac == "X": # lze napsat hezcejc, ale to jeste neumite
            hrac = "O"
        else:
            hrac = "X"
    vytiskni()
# sice to vypada ze to hodne hatim ale libi se mi to
# je to presne jak jsem si to predstavoval
# cili exactly co jsem od vas ocekaval
