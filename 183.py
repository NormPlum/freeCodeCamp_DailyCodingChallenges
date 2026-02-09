# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-09

def ski_jump_medal(distance_points, style_points, wind_comp, k_point_bonus):
    scores = [165.5, 172.0, 158.0, 180.0, 169.5, 175.0, 162.0, 170.0]
    scores.sort(reverse = True)

    my_score = distance_points + style_points + wind_comp + k_point_bonus

    for place, score in enumerate(scores):
        if my_score > score:
            match place:
                case 0:
                    return "Gold"
                case 1:
                    return "Silver"
                case 2:
                    return "Bronze"
                case _:
                    return "No Medal"
