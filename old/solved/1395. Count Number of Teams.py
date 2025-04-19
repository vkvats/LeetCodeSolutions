class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = {num: idx for idx, num in enumerate(rating)}
        tmp = 0
        for num, idx in count.items():
            for n, i in count.items():
                if n != num:
                    if n > num and i > idx:
                        for n2, i2 in count.items():
                            if n2 not in (n, num):
                                if (n2 > n) and (i2 > i):
                                    tmp += 1
                    elif n < num and i > idx:
                        for n3, i3 in count.items():
                            if n3 not in (num, n):
                                if (n3 < n) and (i3 > i):
                                    tmp += 1
        return tmp
# improved method 2 using sliced array

class SolutionM2:
    def numTeams(self, rating: List[int]) -> int:
        count = {num: idx for idx, num in enumerate(rating)}
        tmp = 0
        items = [(key,val) for key, val in count.items()]
        for num, idx in items:
            for n,i in items[idx+1:]:
                if n != num:
                    if n > num and i > idx:
                        for n2, i2 in items[i+1:]:
                            if n2 not in (n, num):
                                if (n2 > n ) and (i2 > i):
                                    tmp += 1
                    elif n < num and i >  idx:
                        for n3, i3 in items[i+1:]:
                            if n3 not in (num, n):
                                if (n3 < n) and (i3 > i):
                                    tmp += 1
        return tmp


# Solution from leetcode
from bisect import bisect_right, bisect_left, insort
class Solution:
    def numTeams(self, r: List[int]) -> int:
        def nteams(r):
            a, res = [], 0
            left, right = [0] * len(r), [0] * len(r)
            for i in range(len(r)):
                left[i] = bisect_left(a, r[i])
                insort(a, r[i])
            a = []
            for i in range(len(r)-1, -1, -1):
                right[i] = len(a) - bisect_right(a, r[i])
                insort(a, r[i])
            for i in range(len(r)):
                if left[i] != 0 and right[i] != 0:
                    res += (left[i] * right[i])
            return res
        return nteams(r) + nteams(r[::-1])

# high fi soluion
class BIT:
    """A Binary Index Tree, a.k.a. Fenwick Tree."""

    def __init__(self, n: int):
        self.n = n
        self.bits = [0] * (n + 1)
        self.total = 0

    # Total stores the total sum of the tree. This makes retrieving right sums more efficient.

    def update(self, index: int, value: int):
        """Add value `value` at index `index`: O(log(n))."""
        index += 1
        self.total += value
        while index <= self.n:
            self.bits[index] += value
            index += index & (-index)

    def getsum(self, index: int):
        """Get the sum of values to the left of `index` if positive, or to the right if negative; O(log(n))."""
        if index < 0:
            # `~index == - index - 1`.
            # `bit.getsum(~index)` will retrieve the sum of values from `index + 1` to `n`.
            return self.total - self.getsum(~index)
        if index >= self.n:
            return self.total
        ans = 0
        index += 1
        while index > 0:
            ans += self.bits[index]
            index -= index & (-index)
        return ans


class SolutionF1:

    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        mapping = {r: i for i, r in enumerate(sorted(rating))}
        left_counts = BIT(n)
        right_counts = BIT(n)
        for r in rating[1:]:
            right_counts.update(mapping[r], 1)
        ans = 0
        left_counts.update(mapping[rating[0]], 1)
        for r in rating[1: -1]:
            index = mapping[r]
            right_counts.update(index, -1)
            ans += left_counts.getsum(index) * right_counts.getsum(~index)
            ans += left_counts.getsum(~index) * right_counts.getsum(index)
            left_counts.update(index, 1)
        return ans