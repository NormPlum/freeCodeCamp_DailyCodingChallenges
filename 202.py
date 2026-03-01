# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-28

import re

def add_punctuation(sentences):
    result = re.sub("(\s[A-Z])", r".\1", sentences)
    return result + "."
