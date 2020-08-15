# New Method
# using bit manipulation
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        output = start
        count = 1
        while count < n:
            start += 2
            output ^= start
            count += 1
        return output


class Solutionf:
    def xorOperation(self, n: int, start: int) -> int:
        array = []
        xor = None
        l = 0
        while l < n:
            num = start + 2*l
            if not xor:
                xor = num
            else:
                xor = xor^num
            # array.append(num)
            l += 1
        output = None
        return xor

if __name__ == '__main__':
    n = 5
    print(Solution().xorOperation(n, 0))