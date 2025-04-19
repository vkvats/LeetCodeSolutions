# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# New solution
# improved version of binary search
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n ==1 : return 1
        lo, hi = 1, n
        while lo < hi:
            mid = lo + (hi - lo)//2
            if isBadVersion(mid):
                hi = mid
            else: lo = mid+1
        return lo

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n ==1 : return 1
        low = 0
        high = n
        while low < high:
            mid = (low + high)//2
            flag = isBadVersion(mid)
            if flag:
                if not isBadVersion(mid-1):
                    return mid
                else:
                    high = mid
            else:
                low = mid + 1
        return low

# Solution from leetcode
