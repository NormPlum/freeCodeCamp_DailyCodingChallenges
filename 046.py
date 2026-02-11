# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-25

def second_largest(arr):
    unique = list(set(arr))
    unique.sort()
    return unique[-2]
