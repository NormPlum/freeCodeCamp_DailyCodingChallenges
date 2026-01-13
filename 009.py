# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-08-19

def sum_of_squares(n):
    result = 0
    for i in range(1, n+1):
        result += i * i
    return result
