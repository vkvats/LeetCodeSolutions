class Solution:
    def findMin(self, nums: [int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi)//2
            if nums[mid] < nums[hi]:
                hi = mid
            elif nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi -= 1
        return nums[lo]

# Solution from leetcode
class SolutionF1:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-1
        while lo < hi:
            if nums[lo] < nums[hi]:
                break
            mid = (lo + hi)//2
            if nums[lo] == nums[mid] == nums[hi]: # separate condition
                lo += 1
                hi -= 1
            elif nums[lo] <= nums[mid]: lo = mid + 1
            else: hi = mid
        return nums[lo]

# Solution from leetcode
class SolutionF2:
    def findMin(self, nums: List[int]) -> int:
        for x,y in zip(nums,nums[1:]):
            if y < x:
                return y
        return nums[0]


nums = [2,2,2,2,0,2,2,2]
target = 0
print(Solution().findMin(nums))

