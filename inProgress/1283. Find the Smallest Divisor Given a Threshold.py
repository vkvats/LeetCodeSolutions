# faster way to find ceiling of number after division
# (num -1)//divisor + 1
    # We ave to search in monotonic space.
    # which makes is suitable for binary search

class Solution:
    def smallestDivisor(self, nums: [int], threshold: int) -> int:

        def condition(divisor):
            return sum((num -1)//divisor + 1 for num in nums) <= threshold

        lo, hi = 1, max(nums)
        while lo < hi:
            mid = (lo + hi)//2
            if condition(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo

if __name__ ==  '__main__':
    nums = [1,2,5,9]
    t = 6
    print(Solution().smallestDivisor(nums, t))