# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-11

def golf_score(par, strokes):
    terms = {
        -2: "Eagle",
        -1: "Birdie",
        0: "Par",
        1: "Bogey",
        2: "Double bogey",
    }

    relative_score = strokes - par

    if strokes == 1:
        return "Hole in one!"
    elif relative_score in terms.keys():
        return terms[relative_score]
    else:
        return relative_score
