class Solution:
    def numIdenticalPairs(self, nums: [int]) -> int:
        count = 0
        for index, val in enumerate(nums):
            for val2 in nums[index + 1:]:
                if val == val2:
                    count += 1
        return count


class Solution:
    def numIdenticalPairs(self, nums: [int]) -> int:
        return sum(1 for i in range(len(nums)) for j in range(i+1, len(nums)) if nums[i] == nums[j])