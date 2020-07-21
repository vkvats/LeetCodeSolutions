class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k != 0:
            nums[:] = nums[-k:] + nums[:len(nums) - k]
        # k = k % len(nums)
        # for i in range(k):
        #     val = nums.pop()
        #     nums.insert(0,val)

# Solution from leetcode
class SolutionF1:
    def rotate(self, nums: [int], k: int) -> None:
        if k <= len(nums) and k != 0:
            nums[:] = nums[-k:]+nums[:len(nums)-k]
        elif k > len(nums):
            k = k - len(nums)
            if k != 0:
                nums[:] = nums[-k:]+nums[:len(nums)-k]