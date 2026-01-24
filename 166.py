# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-23

def is_valid_hex(s):
    hexadecimal_characters = ["#", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]

    if s[0] != "#":
        return False
    elif len(s) != 4 and len(s) != 7:
        return False
    
    for char in s:
        if char.lower() not in hexadecimal_characters:
            return False
    
    return True
