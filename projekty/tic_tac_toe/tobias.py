
pisk = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]

player = 'x'

def print_board(pisk): # beres board jako argument - super

    for x in pisk: # sice se ti tam dela jedna cara navic ale je to elegantni
                   #  takze super
        print(f'{x[0]} | {x[1]} | {x[2]}')
        print('--+---+--')

def check():
    for i in range(3): # pouzivas cykly, taky fajn protoze si zjednodussujes praci
        if pisk[i][0] == pisk[i][1] and pisk[i][1] == pisk[i][2] and pisk[i][1] != ' ':
            print('Player ' + player + ' is the winner!!!')
            return True
    for i in range(3):
        if pisk[0][i] == pisk[1][i] and pisk[1][i] == pisk[2][i] and pisk[1][i] != ' ':
            print('Player ' + player + ' is the winner!!!')
            return True
    for i in range(1): # range(1).. hmm, tady to nesedi, vysral bych se na loop
                       # kdybys delal cykly cyklu a mel misto `1` nejakou promennou pak pohoda
        if pisk[i][i] == pisk[i + 1][i + 1] and pisk[i + 1][i + 1] == pisk[i + 2][i + 2] and pisk[i + 1][i + 1] != ' ':
            print('Player ' + player + ' is the winner!!!')
            return True
    for i in range(1): 
        if pisk[i][i + 2] == pisk[i + 1][i + 1] and pisk[i + 1][i + 1] == pisk[i + 2][i] and pisk[i + 1][i + 1] != ' ':
            print('Player ' + player + ' is the winner!!!')
            return True
    if pisk[0][0] != ' ' and pisk[0][1] != ' ' and pisk[0][2] != ' ' and pisk[1][0] != ' ' and pisk[1][1] != ' ' and pisk[1][2] != ' ' and pisk[2][0] != ' ' and pisk[2][1] != ' ' and pisk[2][2] != ' ': # husty, ale slo by to vymyslet lip
        print('Draw') # printy - chytrejsi je vracet to co se ma vytisknout jako string
                      # lepsi zvyk protoze printy jsou vedlejsi efekty
        return True
    return False

while True:
    print_board(pisk)
    print('Now plays player ' + player) # "now plays player" lol
    print('Enter coordinates: ')
    r = input('Row (0,1,2):')
    c = input('Column(0,1,2): ')
    if r == '0' or r == '1' or r == '2' and c == '0' or c == '1' or c == '2':
        if pisk[int(r)][int(c)] == ' ':
            pisk[int(r)][int(c)] = player
            if check(): # chezky ze sis uvedomil ze `check` vraci bool
                break
            if player == 'x': # jde udelat chytreji, ale to jeste neumite
                player = 'o'
            elif player == 'o': # zbytecnej elif, staci else
                player = 'x'
        else:
            print('Kill yourself! That position is already taken!') # lol nice
    else:
        print('Wrong input you idiot!')
print('End of the game')
# jinak vsechno funguje - super
