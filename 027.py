# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-06

def rotate(matrix):
    # Make a copy of the matrix.
    rotated = []
    for row in matrix:
        rotated.append(row[:])

    # Go through and add numbers to the appropriate place in the copy.
    j = len(matrix) - 1
    for row in matrix:
        i = 0
        for num in row:
            rotated[i][j] = num
            i += 1
        j -= 1

    return rotated
