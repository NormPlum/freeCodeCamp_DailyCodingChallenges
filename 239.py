# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-06

from datetime import datetime, timezone

def get_day_of_week(timestamp):
    date = datetime.fromtimestamp(timestamp / 1000, timezone.utc)
    return date.strftime("%A")
