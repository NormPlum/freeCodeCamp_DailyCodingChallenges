# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-02

def capitalize_fibonacci(s):
    numbers = fibonacci_numbers(len(s))
    string = ""

    for i, char in enumerate(s):
        if i in numbers:
            string += s[i].upper()
        else:
            string += s[i].lower()

    return string


def fibonacci_numbers(length):
    numbers = [0, 1]
    if length > 2:
        for i in range(2, length):
            numbers.append(numbers[i-2] + numbers[i-1])
    return numbers
