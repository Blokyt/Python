x=3
y=3
board = []

def initialise_board(x,y,board):
    board.clear()
    for lign in range(y):
        board.append(x*[" "])
    print_board(board)

def print_board(board):
    for lign in board:
        lign_custom = "|"+"|".join(lign)+"|"
        print(lign_custom)

initialise_board(x,y,board)

def place_token(column,token,board):
    if 0 < column < len(board)+1:
        for i in range(len(board)):
            if board[len(board)-1-i][column-1] == " ":
                board[len(board)-1-i][column-1] = token
                return print_board(board)
    place_token(int(input()),token,board)



while True :
    place_token(int(input()),"O",board)
    place_token(int(input()),"X",board)
