# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-20

def number_of_files(file_size, file_unit, drive_size_gb):
    total_bytes = drive_size_gb * 1000 * 1000 * 1000
    file_bytes = file_size
    match file_unit:
        case "MB":
            file_bytes = file_size * 1000 * 1000
        case "KB":
            file_bytes = file_size * 1000
    return int(total_bytes/ file_bytes)
