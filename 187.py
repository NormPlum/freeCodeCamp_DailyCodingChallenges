# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-13

def get_fastest_speed(times):
    segments = [320, 280, 350, 300, 250]

    speeds = []
    for i, time in enumerate(times):
        speeds.append(segments[i] / time)

    fastest = [0, 0]
    for i, speed in enumerate(speeds):
        if speed > fastest[0]:
            fastest = [speed, i+1]

    return f"The luger's fastest speed was {fastest[0]:.2f} m/s on segment {fastest[1]}."
