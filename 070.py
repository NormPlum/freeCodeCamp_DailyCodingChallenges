# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-19

import re

def extract_attributes(element):
    attributes = []
    matches = re.findall("\s+(\w+=\"[a-zA-Z0-9- ]+\")", element)
    for match in matches:
        parts = re.split("=\"", match.strip('"'))
        attributes.append(parts[0] + ", " + parts[1])
    return attributes
