# ChessRules
# (50 points)
#
# Fill the code in the code structure provided below for ChessRules. The main use of the code block is to write
# functions to design the rules for movement of each piece on the board. This block will also contain the function to
# check if the current player is in check, check-mate. You can also have functions that can return the current player's
# pieces that have legal moves in the current board state.
#
# Following are some suggested functions with the pseudocode provided. You can create/remove functions as needed.


# return True if the input move (from-square and to-square) is legal, else False
# this is the KEY function which contains the rules for each piece type
def IsMoveLegal(piece, from_square, to_square, board):
    # input is from-square and to-square
    # use the input and the board to get the from-piece and to-piece

    # if from-square is the same as to-square
    # return False
    if from_square == to_square:
        return False

    # if the from-piece is a "pawn"
        ## case - pawn wants to move one step forward (or backward if white)
        # if to-square is empty and is in the same column as the from-square
            # return True
    ## case - pawn can move two spaces forward (or backward if white) ONLY if pawn on starting row
    # else if to-square is empty and from-square-row = 2 (or 7 if white) and to-square-row = from-square-row + 2 (or -2 if white)
        # if IsClearPath() - a clear path exists between from-square and to-square
            # return True
    ## case - pawn attacks the enemy piece if diagonal
    # else if there is piece diagonally forward (or backward if white) and that piece belongs to the enemy team
        # return True

    # case pawn
    # if (board[from_square[0][from_square[1]]] == 'p' or board[from_square[0][from_square[1]]] == 'P'):
    # if piece.lower == 'p':
    #     # if its empty and in the same column
    #     if (board[to_square[0][to_square[1]]] == '.' and to_square[0] == from_square[0]):
    #         return True
    #
    #     ## case - pawn can move two spaces forward (or backward if white) ONLY if pawn on starting row
    #     elif board[to_square[0][to_square[1]]] == '.' and (from_square[1] == 2 or from_square[1] == 1) and to_square[
    #         1] == (from_square[1] + 2 or from_square[1] - 2):
    #         if IsClearPath(from_square, to_square):
    #             return True
    #     elif

    # else if the from-piece is a "rook"
        # if to-square is either in the same row or column as the from-square
            # if to-square is either empty or contains a piece that belongs to the enemy team
                # if IsClearPath() - a clear path exists between from-square and to-square
                    # return True

    # else if the from-piece is a "bishop"
        # if to-square is diagonal wrt from-square
            # if to-square is either empty or contains a piece that belongs to the enemy team
                # if IsClearPath() - a clear path exists between from-square and to-square
                    # return True

    # else if the from-piece is a "queen"
        ## SAME as "rook"
        # if to-square is either in the same row or column as the from-square
            # if to-square is either empty or contains a piece that belongs to the enemy team
                # if IsClearPath() - a clear path exists between from-square and to-square
                    # return True
    ## SAME as "bishop"
    # if to-square is diagonal wrt from-square
        # if to-square is either empty or contains a piece that belongs to the enemy team
            # if IsClearPath() - a clear path exists between from-square and to-square
                # return True

    # else if the from-piece is a "knight"
        # calculate the col-diff = to-square-col - from-square-col
        # calculate the row-diff = to-square-row - from-square-row
        # if to-square is either empty or contains a piece that belongs to the enemy team
            # return True for any of the following cases:
                # col-diff = 1 & row_dif = -2
                # col-diff = 2 & row_dif = -1
                # col-diff = 2 & row_dif = 1
                # col-diff = 1 & row_dif = 2
                # col-diff = -1 & row_dif = -2
                # col-diff = -2 & row_dif = -1
                # col-diff = -2 & row_dif = 1
                # col-diff = -1 & row_dif = 2

    # else if the from-piece is a "king"
        # calculate the col-diff = to-square-col - from-square-col
        # calculate the row-diff = to-square-row - from-square-row
    # if to-square is either empty or contains a piece that belongs to the enemy team
        # return True for any of the following cases:
        # abs(col-diff) = 1 & abs(row_dif) = 0
        # abs(col-diff) = 0 & abs(row_dif) = 1
        # abs(col-diff) = 1 & abs(row_dif) = 1

    # return False - if none of the other True's are hit above


# gets a list of legal moves for a given piece
# input = from-square
# output = list of to-square locations where the piece can move to
# def GetListOfLegalMoves():
    # input is the current player and the given piece as the from-square
    # initialize the list of legal moves, i.e., to-square locations to []
    # go through all squares on the board
    # for the selected square as to-square
    #     call IsMoveLegal() with input as from-square and to-square and save the returned value
    #     if returned value is True
    #         call DoesMovePutPlayerInCheck() with input as from-square and to-square and save the returned value
    #         if returned value is False
    #             append this move (to-square) as a legal move
    # return the list of legal moves, i.e., to-square locations
    #

# gets a list of all pieces for the current player that have legal moves
# def GetPiecesWithLegalMoves():
    # initialize the list of pieces with legal moves to []
    # go through all squares on the board
    # for the selected square
        # if the square contains a piece that belongs to the current player's team
            # call GetListOfLegalMoves() to get a list of all legal moves for the selected piece / square
            # if there are any legel moves
                # append this piece to the list of pieces with legal moves
    # return the final list of pieces with legal moves


# returns True if the current player is in checkmate, else False
# def IsCheckmate():

    # call GetPiecesWithLegalMoves() to get all legal moves for the current player
    # if there is no piece with any valid move
        # return True
    # else
        # return False


# returns True if the given player is in Check state
# def IsInCheck():
    # find given player's King's location = king-square
    # go through all squares on the board
        # if there is a piece at that location and that piece is of the enemy team
            # call IsMoveLegal() for the enemy player from that square to the king-square
            # if the value returned is True
                # return True
            # else
                # do nothing and continue
    # return False at the end


# # helper function to figure out if a move is legal for straight-line moves (rooks, bishops, queens, pawns)
# # returns True if the path is clear for a move (from-square and to-square), non-inclusive
# def IsClearPath():
    # given the move (from-square and to-square)

    # if the from and to squares are only one square apart
        # return True
    # else
    # if to-square is in the +ve vertical direction from from-square
        # new-from-square = next square in the +ve vertical direction
    # else if to-square is in the -ve vertical direction from from-square
        # new-from-square = next square in the -ve vertical direction
    # else if to-square is in the +ve horizontal direction from from-square
        # new-from-square = next square in the +ve horizontal direction
    # else if to-square is in the -ve horizontal direction from from-square
        # new-from-square = next square in the -ve horizontal direction
    # else if to-square is in the SE diagonal direction from from-square
        # new-from-square = next square in the SE diagonal direction
    # else if to-square is in the SW diagonal direction from from-square
        # new-from-square = next square in the SW diagonal direction
    # else if to-square is in the NE diagonal direction from from-square
        # new-from-square = next square in the NE diagonal direction
    # else if to-square is in the NW diagonal direction from from-square
        # new-from-square = next square in the NW diagonal direction

    # if new-from-square is not empty
        # return False
    # else
        # return the result from the recursive call of IsClearPath() with the new-from-square and to-square


# makes a hypothetical move (from-square and to-square)
# returns True if it puts current player into check
# def DoesMovePutPlayerInCheck():
    # given the move (from-square and to-square), find the 'from-piece' and 'to-piece'
    # make the move temporarily by changing the 'board'
    # Call the IsInCheck() function to see if the 'player' is in check - save the returned value
    # Undo the temporary move
    # return the value saved - True if it puts current player into check, False otherwise


