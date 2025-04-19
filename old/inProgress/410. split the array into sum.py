class Solution:
    def splitArray(self, nums: [int], m: int) -> int:
        self.nums = nums
        self.m = m
        # use binary search
        lo, hi = max(self.nums), sum(self.nums)
        while lo < hi:
            mid = (lo + hi)//2
            if self.feasible(mid):
                hi = mid
            else: lo = mid + 1
        return lo

    def feasible(self, threshold):
        count = 1
        total = 0
        for num in self.nums:
            total += num
            if total > threshold:
                total = num
                count += 1
                if count > self.m:
                    return False
        return True