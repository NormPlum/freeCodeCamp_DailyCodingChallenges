# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-25

def decompress(s):
    decompressed = []
    positions = s.split()
    for word in positions:
        if word.isnumeric():
            decompressed.append(positions[int(word)-1])
        else:
            decompressed.append(word)
    return " ".join(decompressed)
