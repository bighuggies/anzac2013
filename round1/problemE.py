import sys


def tile_cut(board):
    board = zip(*board)
    board = [list(row) for row in board]
    count = 0

    for x, col in enumerate(board):
        for y, row in enumerate(col):
            if row == 'W':
                count += 1 if check_i(board, x, y) else 0

    return count


def check_i(board, x, y):
    tetromino = False

    #check left
    if x > 0:
        if board[x - 1][y] is 'I':
            if check_n(board, x - 1, y):
                board[x - 1][y] = '-'
                tetromino = True

    #check top
    if y > 0:
        if board[x][y - 1] is 'I':
            if check_n(board, x, y - 1):
                board[x][y - 1] = '-'
                tetromino = True

    #check right
    if x < len(board) - 1:
        if board[x + 1][y] is 'I':
            if check_n(board, x + 1, y):
                board[x + 1][y] = '-'
                tetromino = True

    #check left
    if y < len(board[0]) - 1:
        if board[x][y + 1] is 'I':
            if check_n(board, x, y + 1):
                board[x][y + 1] = '-'
                tetromino = True

    return tetromino


def check_n(board, x, y):
    #check left
    if x > 0:
        if board[x - 1][y] is 'N':
            board[x-1][y] = '-'
            return True

    #check top
    if y > 0:
        if board[x][y-1] is 'N':
            board[x][y-1] = '-'
            return True

    #check right
    if x < len(board) - 1:
        if board[x + 1][y] is 'N':
            board[x + 1][y] = '-'
            return True

    #check left
    if y < len(board[0]) - 1:
        if board[x][y + 1] is 'N':
            board[x][y + 1] = '-'
            return True

    return False


def main():
    board = []
    answers = []

    for l in sys.stdin:
        l = l.strip()

        if l == "":
            answers.append(tile_cut(board))
            board = []
            continue

        board.append(l)

    answers.append(tile_cut(board))

    for a in answers:
        print(a)

if __name__ == '__main__':
    main()
