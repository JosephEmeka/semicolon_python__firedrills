import unittest
from tic_tac_toe.tic_tac_toe import TicTacToe


class Testtictactoe(unittest.TestCase):

    def test_initial_board(self):
        game = TicTacToe()
        expected_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertEqual(game.board, expected_board)

    def test_make_move_valid(self):
        game = TicTacToe()
        game.make_move(0, 0)
        self.assertEqual(game.board[0][0], 'X')

    def test_make_move_invalid(self):
        game = TicTacToe()
        game.make_move(0, 0)
        game.make_move(0, 0)
        self.assertEqual(game.board[0][0], 'X')

    def test_check_winner_row(self):
        game = TicTacToe()
        game.board = [['X', 'X', 'X'], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertEqual(game.check_winner(), 'X')

    def test_check_winner_column(self):
        game = TicTacToe()
        game.board = [['O', ' ', ' '], ['O', ' ', ' '], ['O', ' ', ' ']]
        self.assertEqual(game.check_winner(), 'O')

    def test_check_winner_diagonal(self):
        game = TicTacToe()
        game.board = [['X', ' ', ' '], [' ', 'X', ' '], [' ', ' ', 'X']]
        self.assertEqual(game.check_winner(), 'X')

    def test_board_is_not_full(self):
        game = TicTacToe()
        game.board = [['X', 'O', 'X'], ['O', 'X', 'O'], ['X', ' ', 'O']]
        self.assertFalse(game.is_board_full())

    def test_board_is_full_true(self):
        game = TicTacToe()
        game.board = [['X', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'O']]
        self.assertTrue(game.is_board_full())


