# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-10

# This code assumes the matrix is made up of columns.
# e.g. [['X', 'X', 'X'], ['O', 'O', 'X'], ['O', 'X', 'O']]
# Equals: X O O
#         X O X
#         X X O

def tic_tac_toe(board):
    # For each column...
    for x, col in enumerate(board):
        # For each row...
        for y, item in enumerate(col):
            # Check the items in the first column or top row.
            if x == 0 or y == 0:
                if check_pos(x, y, board):
                    return board[x][y] + " wins"

    # Nobody won.
    return "Draw"


# Check the appropriate row/column/diagonal from the given position.
def check_pos(x, y, board):
    # Check column.
    if y == 0:
        if board[x][0] == board[x][1] and board[x][0] == board[x][2]:
            return True

    # Check row.
    if x == 0:
        if board[0][y] == board[1][y] and board[0][y] == board[2][y]:
            return True
    
    # Check diagonals.
    if x == 0:
        if y == 0:
            if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
                return True
        elif y == 2:
            if board[0][2] == board[1][1] and board[0][2] == board[2][0]:
                return True
    
    return False
