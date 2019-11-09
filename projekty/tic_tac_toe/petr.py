values = {
    0: " ",
    1: "x",
    2: "o"
}

board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def print_board():
    for i in range(3):
        print("{}|{}|{}".format(values.get(board[i][0]), values.get(board[i][1]), values.get(board[i][2])))
        print("-+-+-")

def get_user_input():
    return [int(i) for i in input().split()]

def check_win():
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
    while not finished:
        print_board()
        print("Hraje {}".format(values.get(plays)))
        inp = False
        while not inp:
            try:
                user_input = get_user_input()
                if board[user_input[0]][user_input[1]] == 0:
                    board[user_input[0]][user_input[1]] = plays
                    if plays == 2:
                        plays = 0
                    plays += 1
                    inp = True
                else:
                    print("Buňka je již obsazena")
            except:
                print("Váš vstup není platný")
        finished = check_win()

    print_board()
    print("Konec hry")

if __name__ == "__main__":
    main()
