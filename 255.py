# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-22

def get_cleanup_score(items):
    values = {
        "bottle": 10,
        "can": 6,
        "bag": 8,
        "tire": 35,
        "straw": 4,
        "cardboard": 3,
        "newspaper": 3,
        "shoe": 12,
        "electronics": 25,
        "battery": 18,
        "mattress": 38,
    }

    score = 0
    bonus = 0
    multiplier = 1

    for i, item in enumerate(items):
        if isinstance(item, list) and item[0] == "rare":
            value = item[1]
        else:
            value = values[item]

            if i > 0 and items[i] == items[i-1]:
                bonus += 1
            else:
                bonus = 0
            value += bonus

        if (i+1) % 5 == 0:
            multiplier += 1
            value *= multiplier

        score += value

    return score
