# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-05-05

def is_narcissistic(n):
    number = str(n)
    length = len(number)
    sum = 0

    for num in number:
        sum += pow(int(num), length)

    if sum == n:
        return True
    else:
        return False
