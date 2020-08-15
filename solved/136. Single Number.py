# new method
# Using Bit manipulation
class Solution:
    def singleNumber(self, nums: [int]) -> int:
        # bit manipulation
        x = nums[0]
        for num in nums[1:]:
            x ^= num # XOR with same number will give zero
        return x

# using Counter
from collections import Counter
class Solution:
    def singleNumber(self, nums: [int]) -> int:
        count = Counter(nums)
        for key, val in count.items():
            if val == 1:
                return key



#Naive method
def singleNumber(nums):
    count = {}
    for num in nums:
        count[num]= count.get(num, 0) + 1
    for key, value in count.items():
        if value ==1:
            return key

# math approach
def singleNumberMath(nums):
    return 2 * sum(set(nums)) - sum(nums)

# best solution of leetcode
def singleNumberBest(nums):
    my_dict = dict()
    for i in nums:
        if i in my_dict:
            my_dict.pop(i)
        else:
            my_dict[i] = 1

    for i in my_dict:
        return i

if __name__ == '__main__':
    nums = [2,2,1]
    print(Solution().singleNumber(nums))