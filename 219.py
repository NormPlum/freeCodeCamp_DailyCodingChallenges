# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-17

def get_milestone(years):
    anniversaries = {
        70: "Platinum",
        60: "Diamond",
        50: "Gold",
        40: "Ruby",
        25: "Silver",
        10: "Tin",
        5: "Wood",
        1: "Paper",
        0: "Newlyweds",
    }

    for year in anniversaries:
        if years >= year:
            return anniversaries[year]
