# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-18

import math

def calculate_start_delays(jump_scores):
    results = []
    highest = max(jump_scores)
    for score in jump_scores:
        results.append(math.ceil((highest - score) * 1.5))
    return results
