# New Method
# Bit manipulation
class Solution:
    def missingNumber(self, nums: [int]) -> int:
        # using Bit manipulation
        [nums.append(n) for n in range(len(nums)+1)]
        bit = nums[0]
        for num in nums[1:]:
            bit ^= num
        return bit


def missingNumber(nums):
    nums_set = set(nums)
    actual_set = set(range(len(nums)+1))
    return list(actual_set - nums_set)[0]
# best solutionm
def missingNumberBest(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)

if __name__ == '__main__':
    nums = [3,0,1]
    # nums = [9,6,4,2,3,5,7,0,1]
    nums =[0]
    print(missingNumber(nums))