# My solution
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        num = ""
        for n in A:
            num += str(n)
        new_num = str(int(num) + K)
        return [int(i) for i in new_num]

# solutions from leetcode
class SolutionF1:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        for i in range(len(A) - 1, -1, -1):
            if not K: break
            K, A[i] = divmod(A[i] + K, 10)
        while K:
            K, a = divmod(K, 10)
            A = [a] + A
        return A

# Solution from leetcode
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        A[-1] += K
        for i in range(-1, len(A)*-1, -1):
            carry, A[i] = divmod(A[i], 10)
            A[i-1] += carry
            if carry == 0:
                break
        if A[0] >= 10:
            A = list(map(int, str(A.pop(0)))) + A
        return A