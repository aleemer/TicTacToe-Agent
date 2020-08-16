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
            

""" function minimax(board, isMaximizingPlayer):

    if current board state is a terminal state :
        return empty move
    
    if isMaximizingPlayer :
        bestMove = -INFINITY 
        for each move in board:
            make move and modify board
            move = minimax(board, false)
            bestMove = evalMax(bestMove, move) 
        return bestMove

    else :
        bestMove = +INFINITY 
        for each move in board:
            make move and modify board
            move = minimax(board, true)
            bestMove = evalMin(bestMove, move) 
        return bestMove """