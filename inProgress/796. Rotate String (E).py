class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        # checks
        if not A and not B: return True
        if len(A) != len(B): return False

        for _ in range(100):
            A = A[-1] + A[:-1]
            # print(A)
            if A == B:
                return True
        return False

# Solutions from leetcode
