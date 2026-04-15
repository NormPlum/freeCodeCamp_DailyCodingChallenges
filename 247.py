# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-14

def get_last_letter(s):
    last = ""

    for char in s:
        if not last:
            last = char

        if ord(char.lower()) > ord(last.lower()):
            last = char

    return last
