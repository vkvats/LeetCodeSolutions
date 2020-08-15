# new Method
# Mathematic method to find sum of digits using divmod()
class Solution:
    def countLargestGroup(self, n: int) -> int:
        count = {}
        max_count = -1
        for num in range(1, n+1):
            digit_sum = 0
            while num > 0:
                num, mod = divmod(num, 10)
                digit_sum += mod
            count[digit_sum] = count.get(digit_sum, 0) + 1
            if count[digit_sum] > max_count:
                max_count = count[digit_sum]
        return sum([1 for value in count.values() if value == max_count])

if __name__ == '__main__':
    n = 13
    print(Solution().countLargestGroup(n))

class Solution1:
    def countLargestGroup(self, n: int) -> int:
        count = {}
        for num in range(1, n+1):
            digit_sum = 0
            for d in str(num):
                digit_sum += int(d)
            count[digit_sum] = count.get(digit_sum, 0) + 1
        max_count = max(count.values())
        output = 0
        for value in count.values():
            if value == max_count:
                output += 1
        return output

# solution from leetcode
class SolutionFast:
    def countLargestGroup(self, n: int) -> int:
        dp = {0: 0}
        counts = [0] * (4 * 9)
        for i in range(1, n + 1):
            quotient, reminder = divmod(i, 10)
            cnt = reminder + dp[quotient]
            dp[i] = cnt
            counts[cnt - 1] += 1
        return counts.count(max(counts))