# new Method
# binary search
class Solution:
    def arrangeCoins(self, n: int) -> int:
        # binary search
        lo, hi = 0, n
        while lo <= hi:
            mid = (lo+hi)//2
            val = mid*(mid+1)//2
            if val == n:
                return mid
            if n < val: hi = mid -1
            else: lo = mid + 1
        return hi


# class Solution1:
#     def arrangeCoins(self, n: int) -> int:
        # for i in range(n + 1):
        #     val = (i*(i+1))//2
        #     if val > n:
        #         return i - 1
        #     elif val == n:
        #         return i
        # floor((-1 + sqrt(1 + 8 * n)) / 2)

if __name__ == '__main__':
    n = 5
    print(Solution().arrangeCoins(n))