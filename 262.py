# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-29

import re

def parse_url_query(url):
    query = {}

    parameter_string = re.search("\?(.*)$", url)
    parameter_string = parameter_string.group(1)

    parameters = re.split("&", parameter_string)
    for parameter in parameters:
        key, value = re.split("=", parameter)
        query[key] = value

    return query
