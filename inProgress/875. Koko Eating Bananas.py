class Solution:
    def minEatingSpeed(self, piles: [int], H: int) -> int:
        self.piles = piles
        self.h = H
        lo, hi = 1, max(self.piles)
        while lo < hi:
            mid = (lo + hi)//2
            if self.feasible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo

    def feasible(self, speed):
        # return sum(math.ceil(pile / speed) for pile in piles) <= H  # slower
        return sum((pile-1)//speed + 1 for pile in self.piles) <= self.h # faster