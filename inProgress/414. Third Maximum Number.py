class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(set((nums))) <= 2:
            return max(nums)
        new_nums = list(set(nums))
        new_nums.sort()
        return new_nums[-3]

# Solution from leetcode
