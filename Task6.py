def is_valid(board, num, row, col):
    # Check row and column for validity
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check 3x3 subgrid for validity
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == ".":
                for num in map(str, range(1, 10)):
                    if is_valid(board, num, row, col):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = "."
                return False
    return True

def solveSudoku(board):
    solve(board)

board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

solveSudoku(board)

for row in board:
    print(row)
