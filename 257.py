# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-24

def compress(s):
    positions = {}
    compressed = []

    for i, word in enumerate(s.split()):
        if word not in positions:
            positions[word] = i+1
            compressed.append(word)
        else:
            compressed.append(str(positions[word]))

    return " ".join(compressed)
