# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-18

import re

def largest_number(s):
    numbers = re.split("[,!?:;]", s)
    largest = float(numbers[0])
    for number in numbers:
        if float(number) > largest:
            largest = float(number)
    return largest
