
class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        return None

    def is_board_full(self):
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True

    def play_game(self):
        while True:
            self.print_board()
            enter_move = int(input("Enter number between 1 and 9: "))
            if 1 <= enter_move <= 9:
                enter_move -= 1
                row = enter_move // 3
                col = enter_move % 3
            else:
                print("Invalid entry. Please try again.")

            self.make_move(row, col)
            winner = self.check_winner()
            if winner:
                self.print_board()
                print(f"Player {winner} wins!")
                break
            if self.is_board_full():
                self.print_board()
                print("It's a draw!")
                break


if __name__ == '__main__':
    game = TicTacToe()
    game.play_game()
