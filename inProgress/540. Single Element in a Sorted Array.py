class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        num = None
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for key, val in count.items():
            if val == 1: return key

# solution from leetcode
class SolutionF1:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        low = 0; high = n-1
        while low < high:
            mid = (low + high) >> 1
            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]
            elif nums[mid] == nums[mid-1]:
                if (mid - low) & 1:
                    low = mid + 1
                else:
                    high = mid - 2
            else:
                if (high - mid) & 1:
                    high = mid - 1
                else:
                    low = mid + 2
        return nums[low]


# Solution from leetcode
# taking two steps in array
class SolutionF3:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        prev = nums[0]
        for i in range(1, len(nums), 2):
            if nums[i] != nums[i-1]:
                return nums[i-1]
        if i != len(nums):
            return nums[i+1]