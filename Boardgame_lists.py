class Board:
    def __init__(self, size):
        self.size = size
        self.board = self.generateBoard()

    def generateBoard(self):
        return [[str(i) + str(m) for m in range(self.size)] for i in range(self.size)]

    def display(self):
        for i in range(self.size):
            print(self.board[i])

    def getNeighboursCells(self, r:int, c:int)->list:
        neighbours = []

        observed_cell = self.board[r][c]

        for row in range(self.size):
            for col in range(self.size):
                cell = self.board[row][col]
                if cell != observed_cell:
                    if -1 <= (r - row) <= 1 and -1 <= (c - col) <= 1:
                        neighbours.append(cell)
        return neighbours

    def getAdjacentCells(self, r:int, c:int)->list:
        adjacents = []

        observed_cell = self.board[r][c]

        for row in range(self.size):
            for col in range(self.size):
                cell = self.board[row][col]
                if cell != observed_cell:
                    if r == row and -1 <= (c - col) <= 1: # Same row
                        adjacents.append(cell)
                    if c == col and -1 <= (r - row) <= 1: # Same col
                        adjacents.append(cell)
        return adjacents

board = Board(5)
board.display()
print(board.getAdjacentCells(1,0))