import random
def random_points(x1,y1,x2,y2):
    x_init = x1 if x1 <= x2 else x2
    x_end = x2 if x1 <= x2 else x1
    y_init = y1 if y1 <= y2 else y2
    y_end = y2 if y1 <= y2 else y1
    x = random.randint(x_init, x_end)
    y = random.randint(y_init, y_end)
    return [x,y]
'''
This type of solution would not work, as the probability of choosing a point randomly is not equal 
so this would give wrong answers. 
'''
# the idea is to make the probability of selecting all the points equal.
# this is done by using weighted probability
import bisect # to use binary search
class Solution:

    def __init__(self, rects):
        self.rects, self.ranges, sm = rects, [], 0
        for x1, y1, x2, y2 in rects:
            sm += (x2 - x1 + 1) * (y2 - y1 + 1)
            self.ranges.append(sm)

    def pick(self):
        x1, y1, x2, y2 = self.rects[bisect.bisect_left(self.ranges, random.randint(1, self.ranges[-1]))]
        return [random.randint(x1, x2), random.randint(y1, y2)]

# Explanation link : https://leetcode.com/problems/random-pick-with-weight/discuss/671439/Python-Smart-O(1)-solution-with-detailed-explanation