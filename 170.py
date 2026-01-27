# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-27

import time

def odd_or_even_day(timestamp):
    date = time.gmtime(timestamp / 1000)
    day = date.tm_mday
    if day % 2 == 0:
        return "even"
    else:
        return "odd"
