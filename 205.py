# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-03

def count_perfect_cubes(a, b):
    count = 0

    if a < b:
        lower = a
        higher = b
    else:
        lower = b
        higher = a

    for i in range(lower, higher+1):
        i = abs(i)
        cube_root = i ** (1/3)
        if int(round(cube_root)) ** 3 == i:
            count += 1

    return count
