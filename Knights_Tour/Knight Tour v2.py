class Board:
    def __init__(self):
        self.board = [["_"] * 8 for _ in range(8)]

    def print_board(self):
        print(" -------------------")
        for i in range(7, -1, -1):
            print(f"{i + 1}| {' '.join(self.board[i])} |")
        print(" -------------------")
        print("   1 2 3 4 5 6 7 8")

    def move_knight(self, pos):
        self.board[pos.y][pos.x] = "X"


class Knight:
    def __init__(self, x, y):
        self.y = y - 1
        self.x = x - 1


def check_input(str):
    try:
        x_i, y_i = list(map(int, str.split(" ")))
    except ValueError:
        return False
    if any([x_i < 1, x_i > 8, y_i < 1, y_i > 8]):
        return False
    return [x_i, y_i]


board = Board()
while True:
    ans = check_input(input("Enter the knight's starting position: "))
    if ans:
        break
    else:
        print("Invalid")
knight = Knight(ans[0], ans[1])
board.move_knight(knight)
board.print_board()