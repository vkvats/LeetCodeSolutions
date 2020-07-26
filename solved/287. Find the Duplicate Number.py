# non binary search apprach
# can also try set() or hashing.
class Solution:
    def findDuplicate(self, nums: [int]) -> int:
        nums.sort()
        for i in range(len(nums) -1):
            if nums[i] == nums[i+1]:
                return nums[i]

# hashing
class SolutionM2:
    def findDuplicate(self, nums: [int]) -> int:
        seen = {}
        for val in nums:
            count = seen.get(val,0) + 1
            if count == 2: return val
            else:
                seen[val] = count