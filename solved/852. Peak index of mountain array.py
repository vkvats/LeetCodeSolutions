class Solution:
    def peakIndexInMountainArray(self, A: [int]) -> int:
        for i in range(1, len(A)):
            if A[i] < A[i-1]:
                return i-1
# Solution from leetcode
# Binary search
class SolutionBinarySeach:
    def peakIndexInMountainArray(self, A: [int]) -> int:
        lo, hi = 0, len(A) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if A[mid] < A[mid + 1]:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo