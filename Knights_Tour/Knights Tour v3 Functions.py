def check_board_size(size):

    try:
        X, Y = list(map(int, size.split(" ")))
    except ValueError:
        return False
    if any([Y < 1, X < 1]):
        return False
    return [X, Y]


def get_board_size():

    while True:
        sz = check_board_size(input("Enter your board dimensions: "))
        if sz:
            break
        else:
            print("Invalid")

    return sz


def check_start(str, cols, rows):
    try:
        x_i, y_i = list(map(int, str.split(" ")))
    except ValueError:
        return False
    if any([x_i < 1, x_i > cols, y_i < 1, y_i > rows]):
        return False
    return [x_i - 1, y_i - 1]


def get_start_pos():
    while True:
        ans = check_start(input("Enter the knight's starting position: "), sz[0], sz[1])
        if ans:
            break
        else:
            print("Invalid")

    return ans


def create_board(rows, cols):

    if rows * cols <= 9:
        board = [["_"] * cols for _ in range(rows)]
    elif 10 <= rows * cols < 100:
        board = [["__"] * cols for _ in range(rows)]
    else:
        board = [["___"] * cols for _ in range(rows)]

    return board


def print_board(rows, cols):

    cell_size = len(board[0][0])
    print(" " + "-" * (cols * (cell_size + 1) + 3))
    for i in range(rows - 1, -1, -1):
        print(f"{i + 1}| {' '.join(board[i])} |")
    print(" " + "-" * (cols * (cell_size + 1) + 3))
    print("   " + " ".join([" " * (cell_size - 1) + str(col + 1) for col in range(cols)]))


def move_knight(col, row):

    cell_size = len(board[0][0])
    if cell_size == 1:
        board[col][row] = 'X'
    elif cell_size == 2:
        board[col][row] = ' X'
    elif cell_size == 3:
        board[col][row] = '  X'

def knight_options(col, row):

    cell_size = len(board[0][0])
    if cell_size == 1:
        board[col][row] = 'O'
    elif cell_size == 2:
        board[col][row] = ' O'
    elif cell_size == 3:
        board[col][row] = '  O'


def possible_moves():

    options = [[-2, -1], [-1, -2], [1, -2], [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1]]
    moves = []

    knight_row = ans[1]
    knight_col = ans[0]

    for x in options:
        moves.append([(x[0] + knight_row), x[1] + knight_col])

    pos_moves = [x for x in moves if (x[0] >= 0 and x[1] >= 0)]

    for x in pos_moves:
        try:
            knight_options(x[0], x[1])
        except IndexError:
            continue


if __name__ == "__main__":
    sz = get_board_size()
    ans = get_start_pos()
    board = create_board(sz[1], sz[0])
    move_knight(ans[1], ans[0])
    possible_moves()
    print_board(sz[1], sz[0])
