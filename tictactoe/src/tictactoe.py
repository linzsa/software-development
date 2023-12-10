class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"

    def print_board(self):
        for i in range(0, 9, 3):
            print(" | ".join(self.board[i:i + 3]))
            if i < 6:
                print("-" * 9)

    def make_move(self, position):
        if self.board[position] == " ":
            self.board[position] = self.current_player
            self.current_player = "O" if self.current_player == "X" else "X"
        else:
            print("Invalid move. Try again.")

    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]

        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                return True

        return False

    def is_board_full(self):
        return " " not in self.board


def main():
    game = TicTacToe()

    while True:
        game.print_board()

        position = int(input(f"Player {game.current_player}, enter your move (1-9): ")) - 1

        if 0 <= position <= 8:
            game.make_move(position)

            if game.check_winner():
                print(f"Player {game.current_player} wins!")
                break
            elif game.is_board_full():
                print("It's a draw!")
                break
        else:
            print("Invalid input. Please enter a number between 1 and 9.")


if __name__ == "__main__":
    main()
