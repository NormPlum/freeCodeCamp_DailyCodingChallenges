# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-02

def sum_letters(s):
    sum = 0
    unicode_diff = 64
    for char in s:
        if char.isalpha():
            sum += ord(char.upper()) - unicode_diff
    return sum
