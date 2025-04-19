def judgeCircle(moves):
    x = 0
    y = 0
    for move in moves:
        if move == "U":
            y +=1
        elif move == "D":
            y -=1
        elif move == "R":
            x +=1
        elif move == "L":
            x -=1

    if x ==0 and y ==0:
        return True
    else:
        return False

# best solution on leetcode
def judgeCircleBest(mvoes):
    return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')

if __name__ == '__main__':
    moves = "UD"
    moves = "LL"
    moves = "RRDD"
    print(judgeCircle(moves))