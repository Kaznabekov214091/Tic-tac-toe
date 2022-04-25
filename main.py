import Board

table = Board.Board()
game = True


def row(board):
    if board[0] != " " and board[0] == board[1] == board[2]:
        return True, board[0]
    if board[3] != " " and board[3] == board[4] == board[5]:
        return True, board[3]
    if board[6] != " " and board[6] == board[7] == board[8]:
        return True, board[6]
    else:
        return False, "-"


def column(board):
    if board[0] != " " and board[0] == board[3] == board[6]:
        return True, board[0]
    if board[1] != " " and board[1] == board[4] == board[7]:
        return True, board[1]
    if board[6] != " " and board[2] == board[5] == board[8]:
        return True, board[6]
    else:
        return False, "-"


def diagonal(board):
    if board[4] != " " and board[0] == board[4] == board[8]:
        return True, board[4]
    if board[4] != " " and board[2] == board[4] == board[6]:
        return True, board[4]
    else:
        return False, "-"


def take_input():
    n = int(input("Enter position 1 to 9\n"))
    if table.board[n - 1] == " ":
        return n
    else:
        print("The cell is full")
        return take_input()


index = 0
while game:
    if index >= 9:
        print("Draw")
        break
    table.show_board()
    pos = take_input()
    if index % 2 == 0:
        table.board[pos - 1] = "O"
        index += 1
    else:
        table.board[pos - 1] = "X"
        index += 1
    if row(table.board)[0]:
        table.show_board()
        print(row(table.board)[1] + " Winner!!!")
        game = False
    if column(table.board)[0]:
        table.show_board()
        print(column(table.board)[1] + " Winner !!!")
        game = False
    if diagonal(table.board)[0]:
        table.show_board()
        print(diagonal(table.board)[1] + " Winner!!!")
        game = False
