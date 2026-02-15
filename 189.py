# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-15

def get_hill_rating(drop, distance, hill_type):
    ratings = {
        "Black": 0.25,
        "Blue": 0.1,
        "Green": 0,
    }

    steepness = drop / distance
    if hill_type == "Downhill":
        steepness = steepness * 1.2
    elif hill_type == "Slalom":
        steepness = steepness * 0.9

    for rating in ratings:
        if steepness > ratings[rating]:
            return rating
