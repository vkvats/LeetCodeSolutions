def checkStraightLine(coordinates):
    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]
    if (y2-y1) !=0:
        slope = (x2-x1)/(y2-y1)
    else:
        slope = None
        for i in range(1,len(coordinates)-1):
            y2 = coordinates[i][1]
            if y1!=y2:
                return False
    for i in range(2, len(coordinates)):
        x2,y2 = coordinates[i]
        if (y2-y1) != 0:
            new_slope = (x2-x1)/(y2-y1)
        else:
            new_slope = None
            for i in range(1, len(coordinates) - 1):
                y2 = coordinates[i][1]
                if y1 != y2:
                    return False
        if slope != new_slope:
            return False
    return True

# solution from leetcode
"""Can also use multiplication instead of division this would avoid division by zero problem """
def checkStraightLineBetter(c)
    for i in range(2, len(c)):
        if ((c[i][1] - c[0][1]) * (c[1][0] - c[0][0]) != (c[1][1] - c[0][1]) * (c[i][0] - c[0][0])):
            return False
    return True

if __name__ == '__main__':
    # coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
    # coordinates = [[1,1],[2,2],[2,1],[3,2]]
    coordinates= [[-3, -2], [-1, -2], [2, -2], [-2, -2], [0, -2]]
    print(checkStraightLine(coordinates))