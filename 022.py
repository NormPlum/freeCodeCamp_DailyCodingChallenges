# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-01

def tribonacci_sequence(start_sequence, length):
    if length < 4:
        return start_sequence[:length]

    for i in range(3, length):
        start_sequence.append(start_sequence[i-3] + start_sequence[i-2] + start_sequence[i-1])
    return start_sequence
