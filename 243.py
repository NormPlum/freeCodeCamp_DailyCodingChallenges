# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-10

def rook_attack(rook1, rook2):
    if rook1[0] == rook2[0]:
        return True
    elif rook1[1] == rook2[1]:
        return True
    else:
        return False
