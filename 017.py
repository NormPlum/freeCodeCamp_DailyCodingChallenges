# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-08-27

def evaluate(numbers, operators):
    result = 0
    j = 0

    for i, num in enumerate(numbers):
        if i == 0:
            result = num
            continue

        match operators[j]:
            case "+":
                result += num
            case "-":
                result -= num
            case "*":
                result *= num
            case "/":
                result /= num
            case "%":
                result %= num

        j += 1
        if j >= len(operators):
            j = 0
        
    return result
