# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-14

def count(text, parameter):
    result = 0
    length = len(parameter)
    for i in range(len(text)-length+1):
        if text[i:i+length] == parameter:
            result += 1
    return result
