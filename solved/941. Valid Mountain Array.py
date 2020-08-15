# New solution
# one pass, no need to calculate max value

class Solution:
    def validMountainArray(self, A: [int]) -> bool:
        n = len(A)
        if n < 3: return False
        # one pass
        # break when peak is reached
        # then check for second condition
        # Also, peak can't be first or last elements
        i = 0
        '''
        # This loop can be shortedned using while-else
        while i+1 < n and A[i] < A[i+1]: i += 1
        else: 
            if i == n - 1 or i == 0: return False
            # walk down 
            while i+1 < n and A[i] > A[i+1]: i += 1
                # this will stop at len(A)
        return i == n-1
        '''
        # walk up
        while i+1 < n:
            if A[i] < A[i+1]: i += 1
            else: break
            # this will stop at peak point
        if i == n - 1 or i == 0: return False
        # walk down
        while i+1 < n:
            if A[i] > A[i+1]: i += 1
            else: break
            # this will stop at len(A)
        return i == n-1

# The same task can be done by varifying the condition from both the end
# and at the end checking that stopping point is same
def validMountainArray(self, A):
    i, j, n = 0, len(A) - 1, len(A)
    while i + 1 < n and A[i] < A[i + 1]: i += 1
    while j > 0 and A[j - 1] > A[j]: j -= 1
    return 0 < i == j < n - 1


if __name__ == '__main__':
    a= [3,5,5]
    print(Solution().validMountainArray(a))

class Solution1:
    def validMountainArray(self, A: [int]) -> bool:
        if len(A) < 3: return False
        max_val = max(A)
        index = A.index(max_val)
        if index == len(A) -1 or index == 0: return False
        for i in range(1, len(A)):
            if i <= index:
                if not A[i] > A[i-1]: return False
            elif i > index:
                if not A[i] < A[i-1]: return False
        return True

# Solution from leetcode
class SolutionF1:
    def validMountainArray(self, A: [int]) -> bool:
        if len(A) < 3:
            return False

        right = 0
        left = 9999

        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                continue
            else:
                right = i - 1
                break

        for i in range(len(A) - 1, 0, -1):
            if A[i] < A[i - 1]:
                continue
            else:
                left = i
                break

        return right == left

#Solution from leetcode (A different method)
class SolutionF2:
    def validMountainArray(self, A: [int]) -> bool:
        if len(A) < 3:
            return False
        increasing = True

        if A[0] > A[1]:
            return False

        for i in range(1, len(A)):
            if increasing:
                if A[i] < A[i - 1]:
                    increasing = False
            else:
                if A[i] >= A[i - 1]:
                    return False
        return not increasing

# solution from leetcode
class SolutionF3:
    def validMountainArray(self, A: [int]) -> bool:

        if not A or len(A) < 3:
            return False

        l = 0
        r = len(A) - 1

        while l < r and A[l] < A[l + 1]:
            l += 1

        if l == 0 or l == r:
            return False

        while l < r and A[r] < A[r - 1]:
            r -= 1

        return l == r