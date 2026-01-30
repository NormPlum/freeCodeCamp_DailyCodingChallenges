# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-07

symbols = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

def parse_roman_numeral(numeral):
    return calculate_values(list(numeral), 0)

def calculate_values(numerals, value):
    if len(numerals) == 0:
        return value

    if len(numerals) > 1 and symbols[numerals[0]] < symbols[numerals[1]]:
        value += symbols[numerals[1]] - symbols[numerals[0]]
        numerals.pop(1)
    else:
        value += symbols[numerals[0]]

    numerals.pop(0)
    value = calculate_values(numerals, value)
    return value
