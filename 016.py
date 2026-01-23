# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-08-26

def decode(s):
    while ")" in s:
        i_end = s.find(")")
        i_start = s.rfind("(", 0, i_end)
        chars = s[i_start+1:i_end]
        s = s.replace("(" + chars + ")", chars[::-1], 1)
    return s
