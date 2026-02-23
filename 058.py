# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-07

def find_landing_spot(matrix):
    danger = {}

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 0:
                danger[(r, c)] = calc_danger(r, c, matrix)

    sort_danger = sorted(danger.items(), key=lambda d: d[1])
    return list(sort_danger[0][0])


def calc_danger(r, c, matrix):
    neighbours = []

    # Above.
    if r-1 in range(len(matrix)):
        neighbours.append(matrix[r-1][c])

    # Left.
    if c-1 in range(len(matrix[r])):
        neighbours.append(matrix[r][c-1])

    # Right.
    if c+1 in range(len(matrix[r])):
        neighbours.append(matrix[r][c+1])

    # Below.
    if r+1 in range(len(matrix)):
        neighbours.append(matrix[r+1][c])

    return sum(neighbours)
