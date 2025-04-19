# New method
# breaking where the condition fails before completing the loop
class Solution:
    def canMakeArithmeticProgression(self, arr: [int]) -> bool:
        if not arr: return False
        n = len(arr)
        if n == 1: return False
        arr.sort()
        d = arr[1] - arr[0]
        for i in range(2, n):
            if arr[i] - arr[i-1] != d: return False
        return True

class Solution:
    def canMakeArithmeticProgression(self, arr: [int]) -> bool:
        if not arr: return False
        if len(arr) == 1: return False
        arr.sort()
        diff = [arr[i] - arr[i-1] for i in range(1, len(arr))]
        return len(set(diff)) == 1

# Solutions from leetcode
class SolutionFormula:
    def canMakeArithmeticProgression(self, arr: [int]) -> bool:
        l=min(arr)
        r=max(arr)
        return 2*sum(arr)==len(arr)*(l+r)

# Solution from leetcode (same method without set)
class SolutionF2:
    def canMakeArithmeticProgression(self, arr: [int]) -> bool:
        arr = sorted(arr)
        arr[0] = arr[1] - arr[0]
        for i in range(1, len(arr)-1):
            if arr[i-1] != arr[i+1] - arr[i]:
                return False
            else:
                arr[i] = arr[i+1] - arr[i]
        return True

# Solution from leetcode
# using property of Arithmatic progression
class SolutionF3:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        i = 0
        while i <= len(arr)-3:
            if (arr[i] - arr[i+1]) != (arr[i+1]-arr[i+2]):
                return False
            i+=1
        return Tru