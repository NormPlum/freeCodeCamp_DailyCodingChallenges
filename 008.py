# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-08-18

def factorial(n):
    if n <= 1:
        return 1
    else:
        result = 1
        for i in range(2, n+1):
            result = result * i
        return result
