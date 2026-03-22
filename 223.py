# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-21

def decode_qr(qr_code):
    matrix = []
    for row in qr_code:
        matrix.append(list(row))

    bottom_right = [[4,4], [4,5], [5,4], [5,5]]
    while True:
        if get_data(bottom_right, matrix) == "1111":
            matrix = rotate(matrix)
        else:
            break

    data = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if [i,j] not in [[0,0], [0,1], [0,4], [0,5], [1,0], [1,1], [1,4], [1,5], [4,0], [4,1], [5,0], [5,1]]:
                data += get_data([[i,j]], matrix)

    return data


def get_data(coords, matrix):
    data = ""
    for coord in coords:
        data += matrix[coord[0]][coord[1]]
    return data


def rotate(matrix):
    rotated = []
    for row in matrix:
        rotated.append(row[:])

    j = len(matrix) - 1
    for row in matrix:
        i = 0
        for num in row:
            rotated[i][j] = num
            i += 1
        j -= 1

    return rotated
