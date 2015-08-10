import random


class Player1():

    def __init__(self):
        self.player = 1
        print "Player 1 Initialized...Awaiting Player 2..."

    def play(self, board, player):

        turn = random.choice(board.moves_allowed())

        board.play()

        return "Fuck off"


if __name__ == '__main__':
    list_here = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print random.choice(list_here)