class Solution:
    def minDays(self, bloomDay: [int], m: int, k: int) -> int:
        def feasible(days):
            bonquets, flowers = 0, 0
            for bloom in bloomDay:
                if bloom > days:
                    flowers = 0
                else:
                    bonquets += (flowers + 1)//k
                    flowers = (flowers + 1)%k
            return bonquets >= m

        if len(bloomDay) < m*k: return -1
        lo, hi = 1, max(bloomDay)
        while lo < hi:
            mid = (lo + hi)//2
            if feasible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo

if __name__ == '__main__':
    bd = [7,7,7,7,12,7,7] #[1,10,3,10,2]
    m, k = 2,3
    print(Solution().minDays(bd, m, k))