# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-25

def scale_image(size, scale):
    w, h = size.split("x")
    new_w = int(w) * scale
    new_h = int(h) * scale
    return str(int(new_w)) + "x" + str(int(new_h))
