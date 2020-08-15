class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            n = n & (n-1)
            count += 1
        return count


if __name__ == '__main__':
    # n = 00000000000000000000000000001011
    print(Solution().hammingWeight(n))