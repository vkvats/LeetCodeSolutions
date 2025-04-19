def getSubsequenceCount(loggedMoves):
    steps = 0
    for move in loggedMoves[1:]:
        if move[0].isalpha():
            steps += 1
        elif move[:2] == "..":
            steps -= 1
    return steps


if __name__ == '__main__':
    mo= ["5", "x/", "y/", "../", "z/", "./"]
    print(getSubsequenceCount(mo))