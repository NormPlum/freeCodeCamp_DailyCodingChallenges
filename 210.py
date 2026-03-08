# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-08

import re

def is_valid_hsl(hsl):
    matches = re.match("hsl\(\s*(\d+)\s*,\s*(\d+)%\s*,\s*(\d+)%\s*\)\s*;?", hsl)

    if not matches:
        return False

    h = int(matches.group(1))
    if h < 0 or h > 360:
        return False

    s = int(matches.group(2))
    if s < 0 or s > 100:
        return False

    l = int(matches.group(3))
    if s < 0 or s > 100:
        return False

    return True
