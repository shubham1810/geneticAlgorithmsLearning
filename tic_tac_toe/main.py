class Board():

    def __init__(self):
        self.board = [['-' for j in range(3)] for i in range(3)]

    def print_board(self):
        print self.board[0]
        print self.board[1]
        print self.board[2]

    def check_winner(self):

        # method to check if a player has won and return the player number who has won.

        return 0


if __name__ == '__main__':
    a = Board()
    a.printBoard()