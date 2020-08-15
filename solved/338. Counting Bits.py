# New Method
# bit manipulation
class Solution:
    def countBits(self, num: int) -> [int]:
        output = []
        for i in range(num + 1):
            output.append(self.count_ones(i)) # f'{i:b}'.count('1')
        return output

    def count_ones(self, num):
        count = 0
        while num != 0:
            num &= (num -1)
            count += 1
        return count

class Solution:
    def countBits(self, num: int) -> List[int]:
        output = []
        for i in range(num + 1):
            binary = bin(i)
            c = binary.count("1")
            output.append(c)
        return output
# Solutions from leetcode
class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]
        dp = [0] * (num + 1)
        dp[0] = 0
        for i in range(1, num + 1):
            dp[i] = dp[i >> 1] + (1 if i & 1 == 1 else 0)
        return dp

# solution from leetcode
