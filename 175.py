# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-01

from datetime import datetime, timedelta

def digital_detox(logs):
    days = {}
    logs.sort()

    for i, log in enumerate(logs):
        day = log.split()[0]
        if day not in days:
            days[day] = 1
        else:
            days[day] += 1
        if days[day] > 2:
            return False

        if i > 0:
            this_date = datetime.fromisoformat(log)
            previous_date = datetime.fromisoformat(logs[i-1])
            diff = this_date - previous_date
            if diff / timedelta(hours=1) < 4:
                return False

    return True
