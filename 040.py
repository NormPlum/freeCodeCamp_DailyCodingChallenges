# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-19

def number_of_photos(photo_size_mb, drive_size_gb):
    mb = drive_size_gb * 1000
    return int(mb / photo_size_mb)
