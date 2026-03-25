# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-25

from datetime import datetime, timedelta

def can_retake(finish_time, current_time):
    finish = datetime.strptime(finish_time, "%Y-%m-%dT%H:%M:%S")
    current = datetime.strptime(current_time, "%Y-%m-%dT%H:%M:%S")
    diff = current - finish

    if diff >= timedelta(days=2):
        return True
    else:
        return False
