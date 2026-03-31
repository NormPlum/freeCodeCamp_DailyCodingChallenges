# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-31

from datetime import datetime, timedelta

def alarm_check(alarm_time, wake_time):
    alarm_start = datetime.strptime(alarm_time, "%H:%M")
    alarm_end = datetime.strptime(alarm_time, "%H:%M") + timedelta(minutes=10)
    wake = datetime.strptime(wake_time, "%H:%M")

    if alarm_end < wake:
        return "late"
    elif alarm_start > wake:
        return "early"
    else:
        return "on time"
