# New Method
# Binary search
class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        # Binary search
        lo,hi = 0, len(nums)-1
        while lo <= hi:
            mid = (lo + hi)//2
            if nums[mid] < target:
                lo = mid + 1
            else: hi = mid-1
        return lo
# Modified binary search
class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        # Binary search
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid
            else: lo = mid + 1
        return lo

class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
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
# binary search
class SolutionF2:
    def searchInsert(self, nums: [int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            pivot = (left + right) // 2

            if nums[pivot] == target: return pivot

            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1

        return left