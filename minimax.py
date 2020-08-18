from board import Board
from board import Move


def findbestMove(board):
    
    """For AI to make its turn"""
    bestScore = -1000
    bestMove = 0
    """All available spots"""
    
    for pos in board.availSpots():
        """Modify board and find score."""
        board.modifyPosition("X", pos)
        score = minimax(board, 0, False)
        
        """If resulting score of move is better, modify."""
        if (score > bestScore):
            bestScore = score
            bestMove = pos
        
        """Undo the move"""
        board.modifyPosition(pos, pos)
    
    return bestMove


def minimax(board, depth, isMax):
    #Base Cases
    if (len(board.availSpots()) == 0):
        return 0
    
    if board.playerWin():
        return -10

    if board.aiWin():
        return 10
    
    #Recursive Step(s)
    if (isMax):
        bestScore = -1000
        for pos in board.availSpots():
            """Modify board and find score."""
            board.modifyPosition("X", pos)
            score = minimax(board, depth+1, False)
        
            """If resulting score of move is better, modify."""
            if (score > bestScore):
                bestScore = score
        
            """Undo the move"""
            board.modifyPosition(pos, pos)
        
        """Return the best score we encounter."""
        return bestScore
        
    else:
        bestScore = 1000
        for pos in board.availSpots():
            """Modify board and find score."""
            board.modifyPosition("O", pos)
            score = minimax(board, depth+1, True)
        
            """If resulting score of move is better, modify."""
            if (score < bestScore):
                bestScore = score
        
            """Undo the move"""
            board.modifyPosition(pos, pos)
        
        """Return the best score we encounter."""
        return bestScore

def game():
    # create board
    gameBoard = Board()
    # denote players
    gameBoard.drawBoard()
    print()
    print("Player is denoted as O")
    print("AI is denoted as X")
    print()

    while gameBoard.movesLeft():
        # ask player to make move -> O
        player1Move = int(input("Enter move desired for player 1: "))
        gameBoard.modifyPosition("O", player1Move)
        print()
        gameBoard.drawBoard()

        # check for victory -> if yes, break
        if (gameBoard.playerWin()):
            print("Player has won the game!")
            return
        
        # check for tie
        if (not gameBoard.movesLeft()):
            print("Draw! Neither player has won.")
            return

        # perform AI move
        aiMove = findbestMove(gameBoard)
        gameBoard.modifyPosition("X", aiMove)
        print()
        gameBoard.drawBoard()

        # check for victory -> if yes, break
        if (gameBoard.aiWin()):
            print("AI has won the game!")
            return
        
        # check for tie
        if (not gameBoard.movesLeft()):
            print("Draw! Neither player has won.")
            return

    print("Draw! Neither player has won.")

def play():
    game()

play()