# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-21

def number_of_videos(video_size, video_unit, drive_size, drive_unit):
    if video_unit not in ["B", "KB", "MB", "GB"]:
        return "Invalid video unit"
    elif drive_unit not in ["GB", "TB"]:
        return "Invalid drive unit"

    drive_bytes = drive_size * 1000 * 1000 * 1000 * 1000
    if drive_unit == "GB":
        drive_bytes /= 1000

    video_bytes = video_size * 1000 * 1000 * 1000
    if video_unit == "MB":
        video_bytes /= 1000
    elif video_unit == "KB":
        video_bytes /= 1000 * 1000

    return int(drive_bytes / video_bytes)
