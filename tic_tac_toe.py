import numpy as np

class TicTacToe:

    def __init__(self):
        self.board = np.empty((3,3))
        self.board[:] = np.nan          # Initializing to NaN values for ease of checking winner
        self.winner = None


    def __repr__(self):
        board_str = ""
        for row_idx, row in enumerate(self.board):
            if row_idx:
                board_str += '-----------\n'
            for col_idx, col in enumerate(row):
                if col_idx:
                    board_str += ' |'
                board_str += ' ' + ('X' if col == 1 else 'O' if col == 2 else ' ')
                if col_idx == 2:
                    board_str += '\n'
        return board_str


    def place(self, row, col, marker):
        if not np.isnan(self.board[row][col]):
            return False
        self.board[row][col] = marker
        self.is_winner()
        return True


    def is_winner(self):
        for line in np.row_stack((self.board, self.board.T, np.diag(self.board), np.diag(self.board))):
            line_unique_count = np.unique(line).size            # line=[NaN, NaN, NaN] will result in 3
            if line_unique_count == 1:
                self.winner = line[0]
                return True
        return False

