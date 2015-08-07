import random


class Player1():

    def __init__(self):
        print "I am the main player"

    def play(self, board, player):

        turn = random.choice(board.moves_allowed())

        board.play()

        return "Fuck off"