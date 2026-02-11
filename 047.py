# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-26

def speeding(speeds, limit):
    speeders = []
    average = 0
    for speed in speeds:
        if speed > limit:
            speeders.append(speed - limit)
    if len(speeders) > 0:
        average = sum(speeders) / len(speeders)
    return [len(speeders), average]
