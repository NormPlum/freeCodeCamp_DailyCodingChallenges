# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-22

def digits_or_letters(s):
    digits = 0
    letters = 0
    for char in s:
        if char.isdigit():
            digits += 1
        elif char.isalpha():
            letters += 1
    if digits > letters:
        return "digits"
    elif letters > digits:
        return "letters"
    else:
        return "tie"
