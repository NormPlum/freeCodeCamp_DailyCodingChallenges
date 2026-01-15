# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-14

def parse_link(markdown):
    link = markdown.split("]")
    text = link[0].strip("[")
    url = link[1].strip("()")
    return '<a href="' + url + '">' + text + '</a>'
