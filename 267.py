# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-05-04

def convert_parsecs(parsecs):
    if parsecs % 2 == 0:
        return parsecs / 2 * 6
    else:
        return parsecs * 2
