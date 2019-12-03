# petr.py
```python
# OPRAVOVAL LUKÁŠ
# Celkový komentář: Hezký, dobře čitelný kód, za mě jsi úplně splnil zadání
# Máš to krátké a výstižné


# Hezký, takhle se to normálně dělává, máš nějaký dict, který ti mapuje internální strukturu na její zobrazení
values = {
    0: " ",
    1: "x",
    2: "o"
}

# Kdybys pak chtěl přidat možnost opakovaného hraní, tak bys tohle musel přesunout do nějakého cyklu dole
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def print_board(): # Celkem pěkný, sice to dělá vedlejší efekty, ale tady to moc nevadí
    for i in range(3):
        print("{}|{}|{}".format(values.get(board[i][0]), values.get(board[i][1]), values.get(board[i][2])))
        print("-+-+-")

def get_user_input(): 
    # Taky profi, jenom snad možná by bylo lepší přesunout kód na kontrolu vstupu sem
    # aby to nemátlo lidi, co čtou kód hlavního cyklu a celkově by to bylo, řekl bych, ucelenější
    return [int(i) for i in input().split()]

def check_win(): 
    # Je vidět, že narozdíl od Matěje umíš cykly
    # Bohužel by to nefungovalo, kdybychom zvětšili herní pole
    # Tahle funkce by mohla brát board jako argument, což by bylo hezčí, 
    # protože by se dala používat flexibilněji a nezávisela na svém umístění
    # Každopádně zadání celkem hezky splněno
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != 0:
            return True
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != 0:
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[1][1] != 0:
        return True
    if board[2][0] == board[1][1] == board[0][2] and board[1][1] != 0:
        return True
    return False

def main():
    finished = False
    plays = 1
    
    # Fajn, tady jsou dva odlišné přístupy (jeden je s break), ale nikdo neví, který z nich použít, takže dobrý:D
    while not finished:
        print_board()
        # Dá se zjednodušit f-stringem, ale tvá verze je kompatibilní i se staršími verzemi Pythonu 3 (<3.5),
        # což taky má své výhody
        print("Hraje {}".format(values.get(plays)))
        inp = False
        while not inp:
            try:
                user_input = get_user_input()
                if board[user_input[0]][user_input[1]] == 0:
                    board[user_input[0]][user_input[1]] = plays
                    # Jenom taková zajímavost - dalo by se to zkrátit na plays = (plays+1)%2
                    # Každopádně je otázka, jestli by to bylo čitelnější, takže jsi udělal dobře
                    if plays == 2: 
                        plays = 0
                    plays += 1
                    inp = True
                else:
                    print("Buňka je již obsazena")
            except:
                # Jenom prosím, nikdy nepoužívat except bez specifikovaného typu chyby
                # Tady by stačilo něco jako `except (IndexError, ValueError):`
                # Vždycky specifikuj typy těch chyb, které zachytáváš, mohlo by se ti totiž stát, že tam bude ještě nějaká další
                # Pak další věc - snaž se, aby byla část v try-except bloku, co nejkratší, 
                # protože opět, co kdybys udělal nějakou nečekanou chybu
                # Ty tady totiž máš i tu logiku na udělání tahu a změnu hráče
                # Každopádně jsem rád, že jsi na try-except vůbec přišel
                print("Váš vstup není platný")
        finished = check_win()

    print_board()
    print("Konec hry")

if __name__ == "__main__":
    # Dobrá konstrukce, hodí se to, když chceš, aby tvůj kód byl také snadno importovatelný jako knihovna
    main()
```