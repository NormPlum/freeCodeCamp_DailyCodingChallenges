# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-17

def check_eligibility(athlete_weights, sled_weight):
    bobsled_weight = {
        1: 162,
        2: 170,
        4: 210,
    }
    total_weight = {
        1: 247,
        2: 390,
        4: 630,
    }
    team_size = len(athlete_weights)

    if sled_weight < bobsled_weight[team_size]:
        return "Not Eligible"

    if sum(athlete_weights) + sled_weight > total_weight[team_size]:
        return "Not Eligible"

    return "Eligible"
