# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-19

def invert_matrix(matrix):
    inverted = matrix.copy()
    unique = list(dict.fromkeys(matrix[0]))

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == unique[0]:
                invert = unique[1]
            else:
                invert = unique[0]
            inverted[i][j] = invert

    return inverted
