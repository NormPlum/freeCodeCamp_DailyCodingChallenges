# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-08-13

def fibonacci_sequence(start_sequence, length):
    # 0-2 length.
    if length == 0:
        return []
    elif length == 1:
        return [start_sequence[0]]
    elif length == 2:
        return start_sequence
    
    # 3+ length.
    for i in range(2, length):
        start_sequence.append(start_sequence[i-2] + start_sequence[i-1])
    return start_sequence
