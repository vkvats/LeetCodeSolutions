# new method
# in order n
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l= s = float('-inf')
        for num in nums:
            if num >= l:
                s = l
                l = num
            elif num > s:
                s = num
        return (l-1)*(s-1)

# this is in order nlog n
def maxProduct(nums):
    nums.sort()
    a,b = nums[-2:]
    return (a-1)*(b-1)

if __name__ == '__main__':
    # nums = [3, 4, 5, 2]
    # nums = [1, 5, 4, 5]
    nums = [3,7]
    print(maxProduct(nums))