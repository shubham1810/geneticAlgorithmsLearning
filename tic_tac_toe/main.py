import random


class Board():

    def __init__(self):
        self.board = [['-' for j in range(3)] for i in range(3)]

    def print_board(self):
        print self.board[0]
        print self.board[1]
        print self.board[2]

    def check_winner(self):

        # method to check if a player has won and return the player number who has won.
        checks = [[self.board[0][0], self.board[0][1], self.board[0][2]], [self.board[1][0], self.board[1][1], self.board[1][2]], [self.board[2][0], self.board[2][1], self.board[2][2]],
                  [self.board[0][0], self.board[1][0], self.board[2][0]], [self.board[0][1], self.board[1][1], self.board[2][1]], [self.board[0][2], self.board[1][2], self.board[2][2]],
                  [self.board[0][0], self.board[1][1], self.board[2][2]], [self.board[0][2], self.board[1][1], self.board[2][0]]]

        for i in checks:
            if len(set(i)) == 1:
                if i[0] == 'X':
                    print 'We have a winner'
                    return 1
                elif i[0] == 'O':
                    print "A winner is still here"
                    return 2

        return 0

    def play(self, player, position):

        if position not in range(0, 9):
            return 404

        if player == 1:
            game_turn = 'X'
            curr_palyer = 2
        else:
            game_turn = 'O'
            curr_palyer = 1
        # method to play the turn of the player and return the next player

        if position == 0:
            self.board[0][0] = game_turn
        elif position == 1:
            self.board[0][1] = game_turn
        elif position == 2:
            self.board[0][2] = game_turn
        elif position == 3:
            self.board[1][0] = game_turn
        elif position == 4:
            self.board[1][1] = game_turn
        elif position == 5:
            self.board[1][2] = game_turn
        elif position == 6:
            self.board[2][0] = game_turn
        elif position == 7:
            self.board[2][1] = game_turn
        elif position == 8:
            self.board[2][2] = game_turn

        win = self.check_winner()
        self.print_board()

        if win:
            print "Player " + str(win) + " Wins the game!"
            return 0

        return curr_palyer

    def board_value_at(self, position):

        if position == 0:
            return self.board[0][0]
        elif position == 1:
            return self.board[0][1]
        elif position == 2:
            return self.board[0][2]
        elif position == 3:
            return self.board[1][0]
        elif position == 4:
            return self.board[1][1]
        elif position == 5:
            return self.board[1][2]
        elif position == 6:
            return self.board[2][0]
        elif position == 7:
            return self.board[2][1]
        elif position == 8:
            return self.board[2][2]

        else:
            return 404

    def moves_allowed(self):
        allowed = []

        if self.board[0][0] == '-':
            allowed.append(0)
        elif self.board[0][1] == '-':
            allowed.append(1)
        elif self.board[0][2] == '-':
            allowed.append(2)
        elif self.board[1][0] == '-':
            allowed.append(3)
        elif self.board[1][1] == '-':
            allowed.append(4)
        elif self.board[1][2] == '-':
            allowed.append(5)
        elif self.board[2][0] == '-':
            allowed.append(6)
        elif self.board[2][1] == '-':
            allowed.append(6)
        elif self.board[2][2] == '-':
            allowed.append(8)

        return allowed


def main():

    player = 1
    new_board = Board()
    turn = random.choice(new_board.moves_allowed())

    print "Fuck this too"


if __name__ == '__main__':
    a = Board()
    print a.play(1, 0)
    print a.play(1, 4)
    print a.play(1, 8)

    print a.board[0][0]