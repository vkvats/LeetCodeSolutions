# New method
# using only math to solve (slower in this case)
class Solution:
    def addToArrayForm(self, A: [int], K: int) -> [int]:
        # using math only to solve
        number = 0
        n = len(A)-1
        for i in range(n, -1, -1):
            number += (10**i)*A[n-i]
        number += K
        if number == 0: return [0]
        output = []
        while number > 0:
            number, mod = divmod(number, 10)
            output.append(mod)
        return output[::-1]


# My solution
class Solution1:
    def addToArrayForm(self, A: [int], K: int) -> [int]:
        num = ""
        for n in A:
            num += str(n)
        new_num = str(int(num) + K)
        return [int(i) for i in new_num]

# solutions from leetcode
class SolutionF1:
    def addToArrayForm(self, A: [int], K: int) -> [int]:
        for i in range(len(A) - 1, -1, -1):
            if not K: break
            K, A[i] = divmod(A[i] + K, 10)
        while K:
            K, a = divmod(K, 10)
            A = [a] + A
        return A

# Solution from leetcode
class Solution2:
    def addToArrayForm(self, A: [int], K: int) -> [int]:
        A[-1] += K
        for i in range(-1, len(A)*-1, -1):
            carry, A[i] = divmod(A[i], 10)
            A[i-1] += carry
            if carry == 0:
                break
        if A[0] >= 10:
            A = list(map(int, str(A.pop(0)))) + A
        return A

if __name__ == '__main__':
    a, k = [1,2,0,0], 34445
    print(SolutionF1().addToArrayForm(a, k))