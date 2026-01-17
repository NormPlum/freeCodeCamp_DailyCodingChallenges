# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-16

def is_integer_hypotenuse(a, b):
    addition = pow(a, 2) + pow(b, 2)
    # 'Square root' is the same as 'to the power of 1/2'.
    hypotenuse = pow(addition, 0.5)
    return hypotenuse == int(hypotenuse)
