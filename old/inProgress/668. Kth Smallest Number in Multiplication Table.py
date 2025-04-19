'''
Explanation link: https://leetcode.com/discuss/general-discussion/786126/python-powerful-ultimate-binary-search-template-solved-many-problems
This is very elegant method of finding kth smallest number.

'''

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def enough(num) -> bool:
            count = 0
            for val in range(1, m + 1):  # count row by row
                add = min(num // val, n)
                if add == 0:  # early exit
                    break
                count += add
            return count >= k

        left, right = 1, n * m
        while left < right:
            mid = left + (right - left) // 2
            if enough(mid):
                right = mid
            else:
                left = mid + 1
        return left

m,n,k = 3,3,5
print(Solution().findKthNumber(m,n,k))