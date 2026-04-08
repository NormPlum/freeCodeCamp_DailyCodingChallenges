# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-08

def is_fizz_buzz(arr):
    for i, item in enumerate(arr):
        if type(item) == int:
            if item % 3 == 0 or item % 5 == 0:
                return False
        else:
            num = get_num(i, arr)
            if item == "Fizz" and num % 3 != 0:
                return False
            elif item == "Buzz" and num % 5 != 0:
                return False
    return True


def get_num(i, arr):
    j = 1
    while True:
        if i+j in range(len(arr)):
            if type(arr[i+j]) == int:
                return arr[i+j] - j
            else:
                j += 1
        else:
            break
    while True:
        if i-j in range(len(arr)):
            if type(arr[i-j]) == int:
                return arr[i-j] + j
            else:
                j -= 1
        else:
            break
