# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-30

def is_in_crossword(char):
    grid = [
        [0, 1, 0, 0, 0, 0, 0, 1],
        [0, 1, 1, 0, 1, 1, 1, 1],
        [0, 1, 0, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0],
        [1, 0, 1, 0, 1, 1, 1, 0],
    ]
    number = ord(char)
    binary = bin(number)
    binary = binary.replace("0b", "").zfill(8)

    for i in range(len(grid)):
        representation = ["", "", "", ""]
        for j in range(len(grid)):
            representation[0] += str(grid[i][j])
            representation[1] += str(grid[j][i])
            representation[2] += str(grid[i][-(j+1)])
            representation[3] += str(grid[-(j+1)][i])
        if binary in representation:
            return True
    return False
