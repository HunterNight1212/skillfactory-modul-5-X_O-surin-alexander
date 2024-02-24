board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# для начала нужна доска
board_size = 3


def drow_board(): # рисуем доску
    print(('-' * 4) * board_size)
    for i in range(board_size):
        print((' ' * 3 + '|') * board_size)
        print('', board[0 + i * board_size], '|', board[1 + i * board_size], '|', board[2 + i * board_size], '|')
        print(('-' * 3 + '|') * board_size)


def XODE(index, player): # условия для хода
    if 9 < index or index < 1 or board[index - 1] in ('X', 'O'):
        return False
    board[index - 1] = player
    return True


def check_win(): # условия победы
    win = False
    win_comb = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    )
    for val in win_comb:
        if board[val[0]] == board[val[1]] and board[val[1]] == board[val[2]]:
            win = board[val[0]]

    return win


def start_game(): # соединяем все в большого мегазорда
    drow_board()
    player = 'X'
    step = 0
    while step < 9 and check_win() == False:
        index = int(input('введите' + player + '. 0 - выход: '))
        if index == 0:
            break
        if XODE(index, player):
            print('хороший ход')

            if player == 'X':
                player = 'O'
            else:
                player = 'X'
            drow_board()
            step += 1
        else:
            print('введите другую координату!')
        if step == 9:
            print('ничья!!!')
    print('победа за: ' + check_win())


print('Welcome to the X_O')
start_game()
