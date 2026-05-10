# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-05-09

def transpose(matrix):
    transposed = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == 0:
                transposed.append([])
            transposed[j].append(matrix[i][j])

    return transposed
