# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-07

def get_element_size(window_size, element_vw, element_vh):
    window_sizes = window_size.split("x")
    width = int(window_sizes[0].strip()) * int(element_vw[:-2]) / 100
    height = int(window_sizes[1].strip()) * int(element_vh[:-2]) / 100
    return str(int(width)) + " x " + str(int(height))
