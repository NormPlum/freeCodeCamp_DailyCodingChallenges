# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-22

def detect_roast(beans):
    bean_types = {
        "'": 1,
        "-": 2,
        ".": 3,
    }

    sum = 0
    for bean in beans:
        sum += bean_types[bean]
    average = sum / len(beans)

    if average > 2.5:
        return "Dark"
    elif average < 1.75:
        return "Light"
    else:
        return "Medium"
