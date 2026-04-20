# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-19

def get_unique_climbs(steps):
    prev = [1, 1]

    for i in range(2, steps+1):
        curr = prev[0] + prev[1]

        if i == steps:
            return curr
        else:
            prev[0] = prev[1]
            prev[1] = curr
