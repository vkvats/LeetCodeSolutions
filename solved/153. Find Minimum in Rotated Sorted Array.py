class Solution:
    def findMin(self, nums: [int]) -> int:
        if len(nums) <= 2: return min(nums)
        # find pivot index
        lo, hi = 0, len(nums) - 1
        while lo < hi: # loop breaks at lo == hi
            mid = (lo + hi)//2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else: hi = mid
        return nums[lo]

#
if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7,8,0]
    print(Solution().findMin(nums))