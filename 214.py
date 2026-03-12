# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-12

def is_valid_domino_chain(dominoes):
    for i in range(1, len(dominoes)):
        if dominoes[i-1][1] != dominoes[i][0]:
            return False
    return True
