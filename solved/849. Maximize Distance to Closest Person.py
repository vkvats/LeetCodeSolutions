class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        dist = set()
        for i in range(1, len(seats) - 1):
            if seats[i] == 0:
                left_arr = seats[:i][::-1]
                right_arr = seats[i + 1:]

                d = min(self.distance(left_arr), self.distance(right_arr))
                dist.add(d)
            else:
                dist.add(0)
        dist.add(seats.index(1))
        # last dist
        dist.add(seats[::-1].index(1))
        print(dist)
        return max(dist)

    def distance(self, arr):
        d = None
        try:
            d = arr.index(1)
            if d is not None: return d + 1
        except:
            pass
        return 999999

# Solution from leetcode
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        consequentZero, ans = 0, 0
        for s in seats:
            if s == 0:
                consequentZero += 1
                ans = max(ans, consequentZero)
            else:
                consequentZero = 0
        ans = (ans + 1) // 2
        return max(ans, seats.index(1), seats[::-1].index(1))