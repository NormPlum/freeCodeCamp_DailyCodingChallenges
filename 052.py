# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-01

def to_decimal(binary):
    result = 0
    i = 0
    for j in range(len(binary)-1, -1, -1):
        result += int(binary[i]) * pow(2, j)
        i += 1
    return result
