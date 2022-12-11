import random

# This class define the object TicTacToe game
# the class define the function and Features of the game
class TicTacToe:
   # constratctor
    def __init__(self):
        self.board = []

   # This function creating the Tic Tac Board
   # The function getting Size range of the board and creating it
    def create_board(self):
        size = input("Enter Size: ")
        size = int(size)
        for i in range(size):
            row = []
            for j in range(size):
                row.append('-')
            self.board.append(row)
   # This function choosing the player random
    def get_random_first_player(self):
        return random.randint(0, 1)
   # This function marks the location the player selected
    def fix_spot(self, row, col, player):
        self.board[row][col] = player
   # The function checks whether a certain player has won,
   # the function checks on the board if there is a diagonal/straight/vertical line
    def is_player_win(self, player):
        win = None
        n = len(self.board)
        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True
   # The function switches between the players' turns
    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'
   # The function prints the current board
    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

   # The main function that runs the game and manages the program,
   # is responsible for the board and objects, uses and calls the program
   # functions and at the end of the game ends and returns control to the
   # main program and then the program ends
    def start(self):
        self.create_board()
        player = 'X' if self.get_random_first_player() == 1 else 'O'
        while True:
            print(f"Player {player} turn")
            self.show_board()
            # taking user input
            row, col = list(map(int, input("Enter row and column numbers Between 1-Size: ").split()))
            print()

            # fixing the spot
            self.fix_spot(row - 1, col - 1, player)

            # checking whether current player is won or not
            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break

            # checking whether the game is draw or not
            if self.is_board_filled():
                print("Match Draw!")
                break

            # swapping the turn
            player = self.swap_player_turn(player)
        # showing the final view of board
        print()
        self.show_board()

# ----------------------- Main -----------------------
if __name__ == "__main__":
   tic_tac_toe = TicTacToe()
   tic_tac_toe.start()