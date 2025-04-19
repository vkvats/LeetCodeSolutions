# using group by function
from itertools import groupby
class Solution:
    def findMaxConsecutiveOnes(self, nums: [int]) -> int:
        return max([len(list(g)) for k, g in groupby(nums)])

def findMaxConsecutiveOnes(nums):
    counter = 0
    max_count = 0
    for num in nums:
        if num ==1:
            counter +=1
        else:
            counter =0
        if max_count< counter:
            max_count = counter
    return max_count

# Two pointer solution

class Solutionf:
    def findMaxConsecutiveOnes(self, nums: [int]) -> int:
        length = -1
        i, j = 0, 0
        while j < len(nums):
            if nums[j] == 1:
                j += 1
                i += 1
            elif nums[j] == 0:
                if i > length:
                    length = i
                i = 0
                j += 1
        if i > length:
            return i
        return length


if __name__ == '__main__':
    nums = [1,1,0,1,1,1]
    # nums = [1,0,1,1,0,1]
    print(Solution().findMaxConsecutiveOnes(nums))