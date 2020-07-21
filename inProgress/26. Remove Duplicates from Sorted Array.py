class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        if len(nums) < 2:
            return len(nums)
        i = 0
        for num in nums[1:]:
            if num != nums[i]:
                i += 1
                nums[i] = num
        return i+1

# My solution
from collections import Counter
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = Counter(nums)
        for val in set(nums):
            for i in range(count[val]-1):
                nums.remove(val)
        return len(nums)

#