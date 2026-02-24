# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-24

from datetime import datetime, timedelta

def count_business_days(start, end):
    weekdays = 0

    start_date = datetime.strptime(start, "%Y-%m-%d")
    end_date = datetime.strptime(end, "%Y-%m-%d")

    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() not in [5, 6]:
            weekdays += 1
        current_date += timedelta(days=1)

    return weekdays
