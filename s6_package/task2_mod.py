MIN_COORD = 1
MAX_COORD = 8

def check_queens(queens):
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1]:
                return False
            if abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
                return False
    return True

def validate_input(coord):
    if len(coord) != 2:
        return False
    x, y = coord
    if not (MIN_COORD <= int(x) <= MAX_COORD) or not (MIN_COORD <= int(y) <= MAX_COORD):
        return False
    return True