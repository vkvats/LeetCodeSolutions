# New method
# One pass solution, not really fast though
class Solution:
    def thirdMax(self, nums: [int]) -> int:
        if len(set((nums))) <= 2:
            return max(nums)
        first, second, third = float('-inf'), float('-inf'), float('-inf')
        for num in set(nums):
            if num > first:
                third = second
                second = first
                first = num
            elif first > num > second:
                third = second
                second = num
            elif second > num > third:
                third = num
        return third


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(set((nums))) <= 2:
            return max(nums)
        new_nums = list(set(nums))
        new_nums.sort()
        return new_nums[-3]


