# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-05-08

from datetime import datetime, timedelta

def medication_reminder(medications, current_time):
    due = []
    current = datetime.strptime(current_time, "%H:%M")

    for med in medications:
        if med[0] == "Mergeflictamine":
            prev = datetime.strptime(med[1], "%H:%M")
            next = prev + timedelta(hours=4)
            due = [next, med[0]]

    times = {
        "07:00": "Debuggamanizole",
        "08:00": "Deployxitrin",
        "13:00": "Debuggamanizole",
        "16:00": "Deployxitrin",
        "21:00": "Debuggamanizole",
    }

    for t in times:
        time = datetime.strptime(t, "%H:%M")
        if time > current and time <= due[0]:
            due = [time, times[t]]
            break

    diff = due[0] - current
    hours = int(diff.seconds / 60 / 60)
    mins = int((diff.seconds / 60) % 60)

    return due[1] + " in " + str(hours) + "h " + str(mins) + "m"
