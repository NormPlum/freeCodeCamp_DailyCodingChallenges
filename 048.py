# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-27

import re

def is_spam(number):
    parts = number.split()
    country_code = parts[0][1:]
    area_code = parts[1][1:-1]
    local = parts[2].split("-")

    if len(country_code) > 2 or country_code[0] != "0":
        return True

    if int(area_code) > 900 or int(area_code) < 200:
        return True

    sum_local = 0
    for char in local[0]:
        sum_local += int(char)
    if str(sum_local) in local[1]:
        return True

    stripped = re.sub("[-+() ]", "", number)
    for i in range(10):
        if f"{i}{i}{i}{i}" in stripped:
            return True

    return False
