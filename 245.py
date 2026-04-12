# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-12

def spiral_matrix(matrix):
    array = []

    while len(matrix):
        matrix, array = get_outer_values(matrix, array)

    return array


def get_outer_values(matrix, array):
    # Top.
    if len(matrix):
        for i in range(len(matrix[0])):
            array.append(matrix[0][i])

    # Right.
    if len(matrix) > 2 and len(matrix[0]):
        for i in range(1, len(matrix)-1):
            array.append(matrix[i][-1])

    # Bottom.
    if len(matrix) > 1:
        for i in range(1, len(matrix[0])+1):
            array.append(matrix[-1][-i])

    # Left.
    if len(matrix) > 2 and len(matrix[0]) > 1:
        for i in range(2, len(matrix)):
            array.append(matrix[-i][0])

    # Remove items.
    if len(matrix):
        del matrix[0]
    if len(matrix):
        del matrix[-1]
    if len(matrix):
        for i in range(len(matrix)):
            del matrix[i][0]
            if len(matrix[0]):
                del matrix[i][-1]

    return [matrix, array]
