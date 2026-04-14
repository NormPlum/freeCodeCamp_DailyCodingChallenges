# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-13

def get_initials(name):
    initials = ""
    for word in name.split():
        initials += word[0].upper() + "."
    return initials
