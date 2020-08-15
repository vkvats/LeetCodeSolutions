# new method
from itertools import chain
class Solution:
    def matrixReshape(self, nums: [[int]], r: int, c):
        one_d = list(chain(*nums))
        if len(one_d) < r*c: return nums
        output = []
        for row_num in range(r):
            output.append(one_d[row_num*c : row_num*c + c])
        return output

# old method