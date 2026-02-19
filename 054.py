# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-03

def check_strength(password):
    criteria_met = 0

    if len(password) >= 8:
        criteria_met += 1
    if password != password.lower() and password != password.upper():
        criteria_met += 1
    for num in range(10):
        if str(num) in password:
            criteria_met += 1
            break
    for char in ["!", "@", "#", "$", "%", "^", "&", "*"]:
        if char in password:
            criteria_met += 1
            break

    if criteria_met < 2:
        return "weak"
    elif criteria_met < 4:
        return "medium"
    else:
        return "strong"
