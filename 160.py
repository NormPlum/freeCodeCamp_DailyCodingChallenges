# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-17

def knight_moves(position):
    col, row = list(position)

    if col in ["C", "D", "E", "F"] and row in ["3", "4", "5", "6"]:
        return 8
    
    if (col in ["B", "G"] and row in ["3", "4", "5", "6"]) or (col in ["C", "D", "E", "F"] and row in ["2", "7"]):
        return 6
    
    if (col in ["A", "H"] and row in ["3", "4", "5", "6"]) or (col in ["C", "D", "E", "F"] and row in ["1", "8"]) or (position in ["B2", "B7", "G2", "G7"]):
        return 4
    
    if position in ["A2", "A7", "B1", "B8", "G1", "G8", "H2", "H7"]:
        return 3
    
    if position in ["A1", "A8", "H1", "H8"]:
        return 2
