# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-06

def navigate_trail(map):
    path = ""

    current = find_start(map)
    next = find_next(map, current, "")
    path += next["dir"]
    while not next["goal"]:
        next = find_next(map, next["pos"], next["dir"])
        path += next["dir"]

    return path


def find_start(map):
    for i, row in enumerate(map):
        for j, cell in enumerate(row):
            if cell == "C":
                return [i, j]


def find_next(map, current, previous):
    result = {
        "dir": "",
        "pos": [],
        "goal": False,
    }

    rows = len(map)
    cols = len(map[0])

    # Check above.
    if current[0] > 0:
        if previous != "D":
            if map[current[0]-1][current[1]] != "-":
                result["dir"] = "U"
                result["pos"] = [current[0]-1, current[1]]

    # Check left.
    if current[1] > 0:
        if previous != "R":
            if map[current[0]][current[1]-1] != "-":
                result["dir"] = "L"
                result["pos"] = [current[0], current[1]-1]

    # Check right.
    if current[1] < cols-1:
        if previous != "L":
            if map[current[0]][current[1]+1] != "-":
                result["dir"] = "R"
                result["pos"] = [current[0], current[1]+1]

    # Check below.
    if current[0] < rows-1:
        if previous != "U":
            if map[current[0]+1][current[1]] != "-":
                result["dir"] = "D"
                result["pos"] = [current[0]+1, current[1]]

    # Check if reached goal.
    if map[result["pos"][0]][result["pos"][1]] == "G":
        result["goal"] = True

    return result
