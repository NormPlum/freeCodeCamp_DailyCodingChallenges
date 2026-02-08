# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-08

def calculate_penalty_distance(rounds):
    penalty = 0
    for targets in rounds:
        penalty += (5 - targets) * 150
    return penalty
