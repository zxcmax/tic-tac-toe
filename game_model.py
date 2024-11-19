class GameModel:
    def __init__(self):
        self.board = []
        self.board_size = 10
        self.current_player = "X"

    def set_board_size(self, size):
        self.board_size = size
        self.reset_board()

    def reset_board(self):
        self.board = [[""] * self.board_size for _ in range(self.board_size)]

    def make_move(self, x, y):
        if 0 <= x < self.board_size and 0 <= y < self.board_size:
            if self.board[y][x] == "":
                self.board[y][x] = self.current_player
                self.current_player = "O" if self.current_player == "X" else "X"
                return True
        return False

    def check_winner(self):
        def check_direction(x, y, dx, dy):
            symbol = self.board[y][x]
            count = 0
            for i in range(5):
                nx, ny = x + i * dx, y + i * dy
                if 0 <= nx < self.board_size and 0 <= ny < self.board_size and self.board[ny][nx] == symbol:
                    count += 1
                else:
                    break
            return count == 5

        for y in range(self.board_size):
            for x in range(self.board_size):
                if self.board[y][x] != "":
                    if any(check_direction(x, y, dx, dy) for dx, dy in [(1, 0), (0, 1), (1, 1), (1, -1)]):
                        return True
        return False
