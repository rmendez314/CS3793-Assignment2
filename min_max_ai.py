# MinMaxAI
# (50 points)
#
# Complete the functions below that will perform a move for the given player using the MinMax AI strategy. One function
# will evaluate the board if a move is performed - give score for each of piece and calculate the score for the entire
# chess board. In the second function you will write actual code for the MinMax strategy and return the move
# (from-piece and to-piece). To get the allocated points, searching should be 2-ply (one Max and one Min). You will
# most likely not need to write any other function, but you can, if needed.
#
# Extra Credit
# (5 points) Modify the above MinMax strategy to be 4-ply (one Max, one Min, one Max, one Min).
# (10 points) Perform alpha-beta pruning for the MinMax strategy.


# def evl():
    # this function will calculate the score on the board, if a move is performed
    # give score for each of piece and calculate the score for the chess board


# def GetMinMaxMove():
    # return the best move for the current player using the MinMax strategy
    # to get the allocated points, searching should be 2-ply (one Max and one Min)

    # Following is the setup for a 2-ply game

    # pieces = GetPiecesWithLegalMoves(curPlayer)
    # for each piece in pieces
        # moves = GetListOfLegalMoves(curPlayer, piece)
        # for move in moves
            # perform the move temporarily
            # enemyPieces = GetPiecesWithLegalMoves(enemyPlayer)
            # for enemyPiece in penemyPiecesieces
                # enemyMoves = GetListOfLegalMoves(enemyPlayer, enemyPiece)
                # for enemyMove in enemyMoves
                    # perform the enemyMove temporarily
                    # res = evl(curPlayer)
                    # update the bestEnemyMove -- this is the MIN player trying to minimize from the 'res' evaluation values
                    # undo the enemyMove
            # update the bestMove -- this is the MAX player trying to maximize from the 'bestEnemyMove' evaluation values
            # undo the move
    # if bestMove found without any doubt, pick that
    # if bestMove not found, pick randomly

    # OPTIONAL -- sometimes automated chess keeps on performing the moves again and again
    # e.g., move king left one square and then move king back - repeat
    # For this you will need to remember the previous move and see if the current best move is not the same and opposite as the previous move
    # If so, pick the second best move instead of the best move

