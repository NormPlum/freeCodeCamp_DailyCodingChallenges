# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-23

import re

def is_mirror(str1, str2):
    str1 = re.sub("[^a-zA-Z]", "", str1)
    str2 = re.sub("[^a-zA-Z]", "", str2)

    for i, char in enumerate(str1):
        if char.isalpha():
            if char != str2[-(i+1)]:
                return False

    return True
