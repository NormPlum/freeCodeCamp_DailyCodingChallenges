# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-07

def get_landing_stance(start_stance, rotation):
    turns = int(abs(rotation / 180))
    if turns % 2 == 0:
        return start_stance
    else:
        return "Goofy" if start_stance == "Regular" else "Regular"
