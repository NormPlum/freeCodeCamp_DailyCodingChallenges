# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-04

def is_valid_equation(equation):
    left, right = equation.split("=")
    left = left.strip().split(" ")
    right = int(right.strip())

    reverse = False
    first = left[0]
    op = left[1]
    second = left[2]
    if len(left) > 3:
        op2 = left[3]
        third = left[4]
        if op2 in ["*", "/"] and op in ["+", "-"]:
            reverse = True

    left_eq = 0
    if reverse:
        left_eq = equate(second, op2, third)
        left_eq = equate(first, op, left_eq)
    else:
        left_eq = equate(first, op, second)
        if len(left) > 3:
            left_eq = equate(left_eq, op2, third)

    return left_eq == right


def equate(num1, op, num2):
    num1 = int(num1)
    num2 = int(num2)

    match op:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2
