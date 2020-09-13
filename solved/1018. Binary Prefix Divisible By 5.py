# New method
class Solution:
    def prefixesDivBy5(self, A):
        for i in range(1, len(A)):
            A[i] += A[i - 1] * 2
        return [a % 5 == 0 for a in A]


print(Solution().prefixesDivBy5([0,1,1]))
# My solution
class Solution1:
    def prefixesDivBy5(self, A: [int]) -> [bool]:
        output = []
        str_A = [str(n) for n in A]
        step = 1
        i = 0
        while i + step <= len(A):
            arr = str_A[i: i + step]
            binary = "".join(arr)
            num = int(binary, 2)
            if num % 5 == 0:
                output.append(True)
            else:
                output.append(False)
            step += 1
        return output


# Solution from leetcode
class SolutionF1:
    def prefixesDivBy5(self, A: [int]) -> [bool]:
        def nums(bits):
            curr = 0
            for bit in bits:
                curr = (2 * curr + bit) % 5
                yield curr

        return [num == 0 for num in nums(A)]

# Solution from leetcode
class SolutionF2:
    def prefixesDivBy5(self, A: [int]) -> [bool]:
        res, accu = [not A[0]], A[0]
        for i in range(1, len(A)):
            accu = ((accu << 1) | A[i]) % 5
            res.append(accu % 5 == 0)
        return res

# Solution from leetcode
class SolutionF3:
    def prefixesDivBy5(self, A: [int]) -> [bool]:
        def yielder():
            n = 0
            for x in A:
                n  = ( 2*n + x ) % 5
                yield not n
        return [*yielder()]