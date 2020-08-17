from board import Board

def play():
    game()

def game():
    
    # create board
    gameBoard = Board()
    # denote players
    print("Player 1 is denoted as X")
    print("Player 2 is denoted as O")
    print()
    
    # perform all these operations while spaces are left on the board, if no spaces left, tie!
    while gameBoard.movesLeft():
        # print 3 x 3 empty board
        gameBoard.drawBoard()
        print()
        
        # ask player 1 to make move -> X
        player1Move = int(input("Enter move desired for player 1: "))
        gameBoard.modifyPosition("X", player1Move)
        gameBoard.drawBoard()
        print()

        # check for victory -> if yes, break
        if (gameBoard.aiWin()):
            print("Player 1 has won the game!")
            return
        
        # ask player 2 to make move -> X
        player2Move = int(input("Enter the move desired for player 2: "))
        gameBoard.modifyPosition("O", player2Move)
        gameBoard.drawBoard()
        print()

        # check for victory -> if yes, break
        if (gameBoard.playerWin()):
            print("Player 2 has won the game!")
            return
    
    print("Tie! Neither player has won.")

play()