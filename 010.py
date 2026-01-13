# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-08-20

def squares_with_three(n):
    count = 0
    for i in range(1, n+1):
        digits = list(str(i * i))
        if '3' in digits:
            count += 1
    return count
