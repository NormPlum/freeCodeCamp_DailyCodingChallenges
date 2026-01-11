# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-08-14

def space_jam(s):
    output = ""
    string = s.replace(" ", "").upper()
    for i in string:
        output += i + "  "
    return output.rstrip()
