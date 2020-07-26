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
