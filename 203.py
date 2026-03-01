# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-01

def is_flat(arr):
    for item in arr:
        if type(item) == list:
            return False
    return True
