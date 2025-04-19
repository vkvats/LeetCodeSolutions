def isRectangleOverlap(rec1, rec2):
    x_low, y_low, x_high, y_high = rec1
    x2_low, y2_low, x2_high, y2_high = rec2
    if x_high <= x2_low or y_high <= y2_low or x_low >= x2_high or y_low >= y2_high:
        return False
    return True

"""Instead of checking for true condition, check for false condition"""
# from solution on leetcode
def isRectangleOverlapSolution(self, rec1, rec2):
    return not (rec1[2] <= rec2[0] or  # left
                rec1[3] <= rec2[1] or  # bottom
                rec1[0] >= rec2[2] or  # right
                rec1[1] >= rec2[3])  # top

if __name__ == '__main__':
    # rec1 = [0,0,2,2]
    # rec2 = [1,1,3,3]
    # rec2 = [0, 0, 1, 1]
    # rec1 = [1, 0, 2, 1]
    rec1 =[2, 17, 6, 20]
    rec2= [3, 8, 6, 20]
    print(isRectangleOverlap(rec1, rec2))