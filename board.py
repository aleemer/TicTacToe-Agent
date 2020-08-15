class Board:

    def __init__(self):
        self.board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.score = 0
    
    def winningBoard(self):
        pass

    def availSpots(self):
        availSpots = []
        for spot in self.board:
            if spot != "X" and spot != "O":
                availSpots.append(spot)
        return availSpots

    def drawBoard(self):
        pass
    