# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-17

import re

def mask(card):
    masked = re.sub("[0-9]", "*", card[:-4])
    return masked + card[-4:]
