# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-05

def get_rotation(n):
    string = str(n)
    if n % len(string) == 0:
        return 0

    rotation = 0
    while True:
        rotation += 1
        string = rotate(string)

        if string == str(n):
            return "none"
        elif int(string) % len(string) == 0:
            return rotation


def rotate(string):
    array = list(string)
    num = array.pop(0)
    array.append(num)
    return "".join(array)
