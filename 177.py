# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-03

def mirror(s):
    result = s
    s_list = list(s)
    s_list.reverse()
    for char in s_list:
        result += char
    return result
