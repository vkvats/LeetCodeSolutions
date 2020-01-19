class Solution:
    def twoSum(self, nums, target: int):
        d = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in d:
                return [d[diff],index]
            else:
                d[value] = index
