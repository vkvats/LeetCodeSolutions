class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]
        flipped = ""
        for char in binary:
            if char == "1":
                flipped += "0"
            elif char == "0":
                flipped += "1"
        return int(flipped, 2)


class SolutionF1:
    def findComplement(self, num: int) -> int:
        t = num
        output = 0
        i = 0

        while t & (t - 1):
            t &= t - 1

        while 1 << i < t:
            if not num & (1 << i):
                output |= 1 << i
            i += 1
        return output

# Solution from leetcode
class SolutionF2:
    def findComplement(self, num: int) -> int:
        count = 0
        temp = num
        mask = 0

        while temp > 0:
            temp = temp >> 1
            count += 1
            mask = mask << 1
            mask = mask | 1

        return ~num & mask