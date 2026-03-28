# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-27

# This challenge has a few bugs (https://github.com/freeCodeCamp/freeCodeCamp/issues/66646)
# but I was able to work around them by assuming:
# - 'r' and 't' weren't meant to be in the 3 unit group, and
# - 50 was the limit to reach, not 60.

def truncate_text(s):
    units = {
        1: "ilI.",
        2: "fjrt ",
        3: "abcdeghkmnopqsuvwxyzJL",
        4: "ABCDEFGHKMNOPQRSTUVWXYZ",
    }

    total = 0
    string = ""
    for char in s:
        if total > 47:
            string = string[:-1]
            break
        for unit in units:
            if char in units[unit]:
                total += unit
                string += char

    if string != s:
        return string + "..."
    else:
        return s
