# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-05-10

import re

def is_valid_isbn_13(s):
    stripped = re.sub("-", "", s)
    if not re.fullmatch("\d{13}", stripped):
        return False

    result = 0
    i = 1
    for num in stripped:
        num = int(num)
        if i % 2 != 0:
            result += num * 1
        else:
            result += num * 3
        i += 1

    if result % 10 == 0:
        return True
    else:
        return False
