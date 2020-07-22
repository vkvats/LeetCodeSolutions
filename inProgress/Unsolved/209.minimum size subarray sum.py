# time limit exceeded
class Solution:
    def minSubArrayLen(self, s: int, nums: [int]) -> int:
        if len(nums) == 1:
            if nums[0] == s:
                return 1
            else: return 0
        j = 0
        step = 1
        while j + step <= len(nums):
            while j + step <= len(nums):
                arr = nums[j: j + step]
                if sum(arr) >= s:
                    return step
                j += 1
            step += 1
            j = 0
        return 0




if __name__ == '__main__':
    s = 11
    nums = [1,2,3,4,5]
    print(Solution().minSubArrayLen(s, nums))