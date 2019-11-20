# Zdar, tady Lukáš
# Taky je v tvém kódu přímo vidět nějaký ten vliv toho C# nebo tak něčeho, 
# protože pojmenováváš věci s velkým písmenem na začátku. Dále jsi také s pojmenováváním trošku nekonzistentní.
# V Pythonu jsou zvyky trochu jiné, ale chyba to samozřejmě není.

# Dobrý, akorát k tomu mám jednu připomínku – 
# tady ukládáš data rovnou v jejich výsledném formátu, ale smysluplnější je ukládat
# data v nějakém jednodušším formátu, který je pak před vypsáním do výsledného formátu převeden,
# protože takto musíš porovnávat políčka s jejich výslednými formáty
board = ["[ ]", "[ ]", "[ ]",
         "[ ]", "[ ]", "[ ]",
         "[ ]", "[ ]", "[ ]"]
player_2 = False
Hra = True
kolo = 1
winner_2 = None

# Lukáš - Docela fajn, vypadá to čitelně
#spuští funkce ve správném pořadí
def tah():
    Tah = Input_pos()
    while Input_chack(Tah) == False: # gay protoze input chack vraci bool - Dawid
        Tah = Input_pos()
    Move(Tah)
    Show()

#zobarí hrací desku
def Show(): # Lukáš - bylo by lepší, kdyby Show bralo board jako argument
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
# Lukáš - tady bereš tah jako argument, ale proč ne board? je to pak takový podivně globální
def Move(tah):
    if Input_chack(tah):
        if player_2:
            x = "O"
        else:
            x = "X"
        board[tah] = "[" + x + "]"
    else:
        pass

# Lukáš - a v tvém komentáři je děsivá pravopisná chyba :^)
# Lukáš - i programátor musí umět pravopis, i když všichni už víme, že programovací jazyky dávají mnohem větší smysl
# Lukáš - (jedna kamarádka mi pořád opravuje chyby, takže už mi to teď taky dost vadí)
#skontroluje platnost vstupu
def Input_chack(index):
    if not board[index] == "[ ]":
        print("pole je již obsazené")
        return Falsetsko
    else:
        return True

#převede array s xy pozicí do indexu
def To_Index(tah):
    index = tah[0] + ((tah[1] - 1) * 3) - 1
    return index

# Lukáš - tohle by se dalo udělat za pomocí cyklů mnohem snadněji, příště to zkus nějak chytřeji
# Lukáš - jakmile začneš psát kód, který se nějak podivně opakuje, tak zkus popřemýšlet, jak by to šlo lépe
# Lukáš - taky by bylo lepší, kdyby Chack bralo board jako argument, je to flexibilnější a znovu použitelné
#skontroluje zde hráč nevyhrál
# Lukáš - další děsivá pravopisná chyba
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
        # Lukáš - tohle je neskutečně matoucí, nechápu proč ti Chack vrací None nebo bool a ne True/False, to by bylo mnohem srozumitelnější
        # Lukáš - ty dokonce ten možný True/False výsledek z Chack ani nevyužiješ
        # Lukáš - mimochodem, když porovnáváš == None, tak je vhodnější použít is None (porovnání identity objektu), protože None existuje pouze jenom jedno pro celý vesmír          
        Hra = False
        if player_2:
            print("Hráč 2 wyhrál v kole", kolo)
        else:
            print("Hráč 1 wyhrál v kole", kolo)
    player_2 = not player_2 # Lukáš - inteligentní
    kolo += 1
    if kolo > 8: # Lukáš - taky inteligentní
        Hra = False
        print("Hra skončila bez výsledku")
