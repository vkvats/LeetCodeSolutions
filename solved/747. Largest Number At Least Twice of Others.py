class SolutionM1:
    def dominantIndex(self, nums: [int]) -> int:
        if len(nums) == 1: return 0
        arr = nums[:]
        arr.sort()
        for i in range(len(nums) - 1):
            if arr[-1] < 2*arr[i]:
                return -1
        return nums.index(arr[-1])

# similar solution as below
class SolutionM2:
    def dominantIndex(self, nums: [int]) -> int:
        if len(nums) == 1: return 0
        arr = nums[:]
        arr.sort()
        index = nums.index(arr[-1])
        return index if arr[-1] >= 2*arr[-2] else -1

# solutions from leetcode
class SolutionF1:
    def dominantIndex(self, nums: [int]) -> int:
        # This method compares the largest element with twice of second largest element.
        # if the condition is satisfied then, condition is true for all. else its false.

        first, second, k = -1, -1, -1
        for i, num in enumerate(nums):
            if num > first:
                first, second, k = num, first, i
            elif num > second:
                second = num
        return k if first >= 2 * second else -1