# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-24

def is_perfect_square(n):
    square = -1
    integer = 0
    while square < n:
        square = integer * integer
        if square == n:
            return True
        else:
            integer += 1
    return False
