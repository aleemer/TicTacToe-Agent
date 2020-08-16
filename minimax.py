from board import Board


def minimax():
    pass

def evaluate():
    print("test")


def main():
    evaluate()

if __name__ == "__main__":
    main()


""" function findBestMove(board):
    bestMove = NULL
    for each move in board :
        if current move is better than bestMove
            bestMove = current move
    return bestMove """


""" function isMovesLeft(board):
    for each cell in board:
        if current cell is empty:
            return true
    return false """

def movesLeft(board):
    for c in board.getBoard():
        if c!="X" and c!="O":
            return True
    return False
            

""" function minimax(board, depth, isMaximizingPlayer):

    if current board state is a terminal state :
        return value of the board
    
    if isMaximizingPlayer :
        bestVal = -INFINITY 
        for each move in board :
            value = minimax(board, depth+1, false)
            bestVal = max( bestVal, value) 
        return bestVal

    else :
        bestVal = +INFINITY 
        for each move in board :
            value = minimax(board, depth+1, true)
            bestVal = min( bestVal, value) 
        return bestVal """