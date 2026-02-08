# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-17

import re

def generate_slug(str):
    slug = str.lower()
    slug = re.sub("[^a-zA-Z0-9 ]", "", slug)
    slugs = slug.split()
    slug = "%20".join(slugs)
    return slug
