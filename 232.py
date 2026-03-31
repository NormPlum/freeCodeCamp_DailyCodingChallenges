# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-30

def get_due_date(date_str):
    month_days = {
        28: [2],
        30: [4,6,9,11],
        31: [1,3,5,7,8,10,12],
    }

    year, month, day = date_str.split("-")

    due_month = int(month) + 9
    due_year = int(year)
    due_day = int(day)

    if due_month > 12:
        due_month -= 12
        due_year += 1

    for month_day in month_days:
        if due_month in month_days[month_day]:
            if due_day > month_day:
                due_day = month_day
                break

    return f"{due_year}-{due_month:02d}-{due_day:02d}"
