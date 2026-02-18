# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-02

def to_binary(decimal):
    remainders = ""

    while True:
        result = int(decimal / 2)
        remainders += str(decimal % 2)
        decimal = result
        if decimal <= 0:
            break

    return remainders[::-1]
