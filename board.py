class Board:

    def __init__(self):
        self.board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.score = 0
    
    def winningBoard(self):
        wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for w in wins:
            if (self.board[w[0]]=="O" and self.board[w[1]]=="O" and self.board[w[2]]=="O"):
                return True
            if (self.board[w[0]]=="X" and self.board[w[1]]=="X" and self.board[w[2]]=="X"):
                return True
        return False

    def availSpots(self):
        availSpots = []
        for spot in self.board:
            if spot != "X" and spot != "O":
                availSpots.append(spot)
        return availSpots

    def drawBoard(self):
        pass
