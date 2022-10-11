
board = [1,2,3,4,5,6,7,8,9]

def print_board(board):
    for i in range(3):
        print(board[0+i*3],'|', board[1+i*3], '|', board[2+i*3])
        



def InputNumber(text):
    is_OK = False
    while not is_OK:
       
        try:
            number =int(input(f"Ваш ход, выберите свободную ячейку {text} от 1 до 9:"))
        except ValueError:
            print('Это не число!')
            continue
        if number >= 1 and number <= 9:
            if(str(board[number-1]) not in 'XO'):
                board[number-1] = text
                is_OK = True
            else:
                print('Занято')
        else:
            print('Это не число от 1 до 9!')

def victory_check(board):
    victory = ((0,1,2),(3,4,5),(6,7,8),
               (0,3,6),(1,4,7),(2,5,8),
               (0,4,8),(2,4,6))
    for i in victory:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            print(board[i[0]])
            return board[i[0]]
    return False

def game(board):
    counter =0
    vic = False
    while not vic:
        print_board(board)
        if counter % 2 == 0:
            InputNumber('X')
        else:
            InputNumber('0')
        counter +=1
        if counter > 4:
            tt_win = victory_check(board)
            if tt_win:
                print_board(board)
                print(tt_win,'Победа')
                vic = True
                break
            if counter == 9:
                print_board(board)
                print('НИЧЬЯ')
                break

game(board)