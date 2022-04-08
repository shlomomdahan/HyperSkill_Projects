def print_board():

    print(" -------------------")
    print("8| " + Board[0][7] + " " + Board[1][7] + " " + Board[2][7] + " " + Board[3][7] + " " + Board[4][7] + " " + Board[5][7] + " " + Board[6][7] + " " + Board[7][7] + " |")
    print("7| " + Board[0][6] + " " + Board[1][6] + " " + Board[2][6] + " " + Board[3][6] + " " + Board[4][6] + " " + Board[5][6] + " " + Board[6][6] + " " + Board[7][6] + " |")
    print("6| " + Board[0][5] + " " + Board[1][5] + " " + Board[2][5] + " " + Board[3][5] + " " + Board[4][5] + " " + Board[5][5] + " " + Board[6][5] + " " + Board[7][5] + " |")
    print("5| " + Board[0][4] + " " + Board[1][4] + " " + Board[2][4] + " " + Board[3][4] + " " + Board[4][4] + " " + Board[5][4] + " " + Board[6][4] + " " + Board[7][4] + " |")
    print("4| " + Board[0][3] + " " + Board[1][3] + " " + Board[2][3] + " " + Board[3][3] + " " + Board[4][3] + " " + Board[5][3] + " " + Board[6][3] + " " + Board[7][3] + " |")
    print("3| " + Board[0][2] + " " + Board[1][2] + " " + Board[2][2] + " " + Board[3][2] + " " + Board[4][2] + " " + Board[5][2] + " " + Board[6][2] + " " + Board[7][2] + " |")
    print("2| " + Board[0][1] + " " + Board[1][1] + " " + Board[2][1] + " " + Board[3][1] + " " + Board[4][1] + " " + Board[5][1] + " " + Board[6][1] + " " + Board[7][1] + " |")
    print("1| " + Board[0][0] + " " + Board[1][0] + " " + Board[2][0] + " " + Board[3][0] + " " + Board[4][0] + " " + Board[5][0] + " " + Board[6][0] + " " + Board[7][0] + " |")
    print(" -------------------")
    print("   1 2 3 4 5 6 7 8")


def start_position():
    while True:
        try:
            row, col = map(int, input("Enter row and column for starting position: ").split())
            if row > 8 or row < 1:
                print('Invalid dimensions!')
                continue
            elif col > 8 or col < 1:
                print('Invalid dimensions!')
                continue
            elif row == 0 or col == 0:
                print('Invalid dimensions!')
                continue
            else:
                break
        except ValueError:
            print('Invalid dimensions!')

    return row, col

def update_start(row, col):

    Board[row-1][col-1] = 'X'
    print_board()


Board = [['_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_']]

if __name__ == "__main__":
    print("Welcome to knights tour! Below is your game board:")
    # print_board()
    row, col = start_position()
    update_start(row, col)
