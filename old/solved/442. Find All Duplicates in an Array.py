# New method
# in place swapping as per index
# to do this we need to have an array that starts from 1 and goes till N
# Then we keep swaping the number at position i with number-1 position,
# number-1 position is the original position of the number. and the repeated numbers
# will be at wrong position by the end.
class Solution(object):
    def findDuplicates(self, nums):
        for i in range(len(nums)):
            while i != nums[i] - 1 and nums[i] != nums[nums[i]-1]:
				nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

        return [nums[it] for it in range(len(nums)) if it != nums[it] - 1]


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        output = []
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                output.append(nums[i])
        return output

# method 2
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        output = []
        count = {}
        for num in nums:
            if num in count:
                output.append(num)
            else:
                count[num] = 1
        return output
    

# solution from leetcode
