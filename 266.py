# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-05-03

from datetime import time

def get_greeting(s):
    parts = s.split(":")
    t = time(int(parts[0]), int(parts[1]))

    if t >= time(5) and t < time(12):
        return "Good morning"
    elif t >= time(12) and t < time(18):
        return "Good afternoon"
    elif t >= time(18) and t < time(22):
        return "Good evening"
    elif t >= time(22) or t < time(5):
        return "Good night"
