# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-08-25

import re

def to_camel_case(s):
    result = ""
    words = re.split("[-_\s]+", s)
    for i, word in enumerate(words):
        if i != 0:
            result += word.title()
        else:
            result += word.lower()
    return result
