# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-11

def compute_score(judge_scores, *penalties):
    judge_scores.sort()
    base = sum(judge_scores) - judge_scores[0] - judge_scores[-1]
    return base - sum(penalties)
