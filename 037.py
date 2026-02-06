# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-16

import re

def capitalize(paragraph):
    return re.sub("(^|[.?!]+)\s*([a-z])", lambda match: match.group(0).upper(), paragraph)
