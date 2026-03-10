# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-16

import re

def validate(email):
    if ".." in email:
        return False

    matches = re.match("^([a-zA-Z0-9._-]*)@([^@]*?\.[a-zA-Z][a-zA-Z]+)$", email)

    if not matches:
        return False

    if matches.group(1).strip(".") != matches.group(1):
        return False

    return True
