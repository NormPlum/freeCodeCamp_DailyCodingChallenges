# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-09

from datetime import datetime, timedelta

def moon_phase(date_string):
    phases = {
        "New": range(1, 8),
        "Waxing": range(8, 15),
        "Full": range(15, 22),
        "Waning": range(22, 29),
    }
    reference_date = datetime(2000, 1, 6)

    date = datetime.strptime(date_string, "%Y-%m-%d")
    diff = date - reference_date + timedelta(days=1)
    day = diff.days % 28

    for phase in phases:
        if day in phases[phase]:
            return phase
