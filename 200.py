# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-26

def count_letters_and_numbers(s):
    letters = 0
    numbers = 0

    for char in s:
        if char.isalpha():
            letters += 1
        elif char.isdecimal():
            numbers += 1

    return f"The string has {letters} letter{'s'[:letters^1]} and {numbers} number{'s'[:numbers^1]}."
