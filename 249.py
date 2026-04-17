# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-16

import re

def do_math(s):
    calc = 0

    # Strip non-digits from start and end.
    s = re.sub("^[^0-9]*", "", s)
    s = re.sub("[^0-9]*$", "", s)

    # Get a list of digits and non-digits.
    digits = list(filter(None, re.split("[^0-9]+(?=[0-9]|$)", s)))
    non_digits = list(filter(None, re.split("[0-9]+(?=[^0-9]|$)", s)))

    # Perform the calculations.
    for i in range(len(digits)):
        if i == 0:
            calc = int(digits[0])
            continue

        if len(non_digits[i-1]) % 2 == 0:
            calc += int(digits[i])
        else:
            calc -= int(digits[i])

    return calc
