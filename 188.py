# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-14

def get_difficulty(track):
    difficulties = {
        "Hard": 200,
        "Medium": 100,
        "Easy": 0,
    }

    difficulty = 0
    for i, turn in enumerate(track):
        if turn == "L" and i > 0 and track[i-1] == "R":
            difficulty += 15
        elif turn == "R" and i > 0 and track[i-1] == "L":
            difficulty += 15
        elif turn == "L" or turn == "R":
            difficulty += 5

    for d in difficulties:
        if difficulty > difficulties[d]:
            return d
