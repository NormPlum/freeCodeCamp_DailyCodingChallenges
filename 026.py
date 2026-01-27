# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-05

def is_valid_ipv4(ipv4):
    numbers = ipv4.split(".")

    for num in numbers:
        if not num:
            return False
        elif num[0] == "0" and len(num) > 1:
            return False
        elif int(num) < 0 or int(num) > 255:
            return False

    return True
