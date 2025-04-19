# New Method
# inplace
class Solution:
    def runningSum(self, nums: [int]) -> [int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
        return nums


def runningsum(nums):
    output = []
    sum=0
    for num in nums:
        sum += num
        output.append(sum)
    return output
## best solution from leetcode
def runningSumBest(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums

import itertools
def runningSum2(nums):
    return itertools.accumulate(nums)


if __name__ == '__main__':
    # nums= [1,2,3,4]
    # nums = [1, 1, 1, 1, 1]
    nums = [3, 1, 2, 10, 1]
    print(runningsum(nums))