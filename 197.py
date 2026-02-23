# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-23

def can_donate(donor, recipient):
    if donor[-1] == "+" and recipient[-1] == "-":
        return False

    if donor[:-1] != "O" and donor[:-1] not in recipient[:-1]:
        return False

    return True
