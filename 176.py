# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-02

def groundhog_day_prediction(appearance):
    if type(appearance) is bool:
        if appearance:
            return "Looks like we'll have six more weeks of winter."
        else:
            return "It's going to be an early spring."
    else:
        return "No prediction this year."
