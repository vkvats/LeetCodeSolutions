class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]: return len(nums)
        for idx, num in enumerate(nums):
            if num == target or num > target:
                return idx

# Solution from leetcode
class SolutionF1:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0

        for num in nums:
            if num >= target:
                return index
            index += 1

        if index == len(nums):
            return len(nums)

# Solution from leetcode
class SolutionF2:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            pivot = (left + right) // 2

            if nums[pivot] == target: return pivot

            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1

        return left