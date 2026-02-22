# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-21

def score_curling(house):
    rings = {
        0: [[2,2]],
        1: [[1,1], [1,2], [1,3], [2,1], [2,3], [3,1], [3,2], [3,3]],
        2: [[0,0], [0,1], [0,2], [0,3], [0,4], [1,0], [1,4], [2,0], [2,4], [3,0], [3,4], [4,0], [4,1], [4,2], [4,3], [4,4]],
    }

    scores = {
        "R": {
            0: 0,
            1: 0,
            2: 0,
        },
        "Y": {
            0: 0,
            1: 0,
            2: 0,
        },
    }

    for x in range(5):
        for y in range(5):
            cell = house[x][y]
            if cell == ".":
                continue

            if [x,y] in rings[0]:
                scores[cell][0] += 1
            elif [x,y] in rings[1]:
                scores[cell][1] += 1
            elif [x,y] in rings[2]:
                scores[cell][2] += 1

    best = {
        "R": 3,
        "Y": 3,
    }
    for team in scores:
        for ring in scores[team]:
            if scores[team][ring] > 0:
                best[team] = ring
                break

    score = 0
    if best["R"] < best["Y"]:
        for i in range(best["Y"]):
            score += scores["R"][i]
        return "R: " + str(score)
    elif best["Y"] < best["R"]:
        for i in range(best["R"]):
            score += scores["Y"][i]
        return "Y: " + str(score)
    else:
        return "No points awarded"
