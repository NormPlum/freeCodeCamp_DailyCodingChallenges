# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-04

def truncate_text(text):
    if len(text) <= 20:
        return text
    else:
        return text[:17] + "..."
