# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-12

def get_number_of_plants(field_size, unit, crop):
    ACRE = 4046.86
    HECTARE = 10000
    PLANTS = {
        "corn": 1,
        "wheat": 0.1,
        "soybeans": 0.5,
        "tomatoes": 0.25,
        "lettuce": 0.2,
    }

    if unit == "acres":
        sq_metres = field_size * ACRE
    else:
        sq_metres = field_size * HECTARE
    
    return int(sq_metres / PLANTS[crop])
