from board import Board


def evaluate():
    print("test")


def main():
    evaluate()

if __name__ == "__main__":
    main()


""" def minimax(board, isMax):
    #Base Cases
    if (len(board.availSpots()) == 0):
        return 0
    
    if board.playerWin():
        return 10

    if board.aiWin():
        return -10
    
    #Recursive Step(s)
    if (isMax):
        # Steps
        minimax(newboard, False)
        pass
    else:
        # Steps
        minimax(newboard, True)
        pass """