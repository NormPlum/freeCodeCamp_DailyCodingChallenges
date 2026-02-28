# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-27

def shift_matrix(matrix, shift):
    length = len(matrix[0])
    sequence = []
    for row in matrix:
        for num in row:
            sequence.append(num)

    if shift > 0:
        while shift > 0:
            last = sequence.pop()
            sequence.insert(0, last)
            shift -= 1
    elif shift < 0:
        while shift < 0:
            first = sequence.pop(0)
            sequence.append(first)
            shift += 1

    result = []
    for i, num in enumerate(sequence):
        if i % length == 0:
            result.append([])
        result[int(i/length)].append(num)

    return result
