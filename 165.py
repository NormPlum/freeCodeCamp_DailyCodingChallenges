# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-22

def get_average_grade(scores):
    grades = {
        "A+": 97,
        "A": 93,
        "A-": 90,
        "B+": 87,
        "B": 83,
        "B-": 80,
        "C+": 77,
        "C": 73,
        "C-": 70,
        "D+": 67,
        "D": 63,
        "D-": 60,
        "F": 0,
    }

    total = 0
    for score in scores:
        total += score
    average = total / len(scores)

    for grade, min_score in grades.items():
        if average >= min_score:
            return grade
