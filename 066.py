# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-15

import re

def strip_tags(html):
    return re.sub("<.*?>", "", html)
