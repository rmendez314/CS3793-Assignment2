# ChessBoard
# (10 points)
#
# Fill the code in the code structure provided below for the ChessBoard. The main use of this code block write
# functions to initialize the board, draw the board, get the board state and move piece. You can add any other
# functions if needed.



class chess_board():
    def __init__(self):
        pass


# you can add/change the input parameters for each function
# you can change the function names and also add more functions if needed


def ChessBoardSetup():
    # initialize and return a chess board - create a 2D 8x8 array that has the value for each cell
    # USE the following characters for the chess pieces - lower-case for BLACK and upper-case for WHITE
    # . for empty board cell
    # p/P for pawn
    # r/R for rook
    # t/T for knight
    # b/B for bishop
    # q/Q for queen
    # k/K for king
    board = [['r', 't', 'b', 'q', 'k', 'b', 't', 'r'],
             ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['R', 'T', 'B', 'Q', 'K', 'B', 'T', 'R']
             ]
    return board


def DrawBoard(chess_board):
    # write code to print the board - following is one print example
    # r t b q k b t r
    # p p p p p p p p
    # . . . . . . . .
    # . . . . . . . .
    # . . . . . . . .
    # . . . . . . . .
    # P P P P P P P P
    # R T B Q K B T R
    for r in chess_board:
        for c in r:
            print(c, end="  ")
        print()


def MovePiece(piece, from_loc, to_loc, board):
    # write code to move the one chess piece
    # you do not have to worry about the validity of the move - this will be done before calling this function
    # this function will at least take the move (from-piece and to-piece) as input and return the new board layout
    board[from_loc[0]][from_loc[1]] = '.'
    board[to_loc[0]][to_loc[1]] = piece
    return board


chess_board = ChessBoardSetup()
# DrawBoard(chess_board)
# chess_board = MovePiece('k', [2,4], [0,4], chess_board)
DrawBoard(chess_board)