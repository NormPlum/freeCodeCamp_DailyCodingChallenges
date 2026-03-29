# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-29

import re

def is_valid_isbn10(s):
    match = re.search("^[0-9-]{12}[0-9X]$", s)
    if not match:
        return False

    characters = re.sub("-", "", s)
    total = 0
    for i, char in enumerate(characters):
        pos = i + 1
        if char == "X":
            total += (10 * pos)
        else:
            total += (int(char) * pos)

    if total % 11 == 0:
        return True
    else:
        return False
