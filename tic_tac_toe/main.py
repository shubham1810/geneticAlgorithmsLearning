class Board():

    def __init__(self):
        self.board = [['-' for j in range(3)] for i in range(3)]

    def printBoard(self):
        print self.board[0]
        print self.board[1]
        print self.board[2]


if __name__ == '__main__':
    a = Board()
    a.printBoard()