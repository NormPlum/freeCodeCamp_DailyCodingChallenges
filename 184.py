# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-10

from datetime import datetime

def get_relative_results(results):
    diff_results = []

    for i, result in enumerate(results):
        if i == 0:
            winning_time = datetime.strptime(result, "%H:%M:%S")
            diff_results.append("0")
        else:
            finish_time = datetime.strptime(result, "%H:%M:%S")
            diff = finish_time - winning_time
            mins, sec = divmod(diff.total_seconds(), 60)
            diff_results.append("+" + str(int(mins)) + ":" + f"{int(sec):02d}")

    return diff_results
