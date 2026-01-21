# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-21

def parse_inline_code(markdown):
    result = ""
    open = False
    for char in markdown:
        if char == "`":
            if open:
                result += "</code>"
                open = False
            else:
                result += "<code>"
                open = True
        else:
            result += char
    return result
