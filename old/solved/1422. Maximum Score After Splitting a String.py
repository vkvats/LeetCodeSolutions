class Solution:
    def maxScore(self, s: str) -> int:
        string = [int(char) for char in s]
        scores = []
        for i in range(1, len(string)):
            left = string[:i].count(0)
            right = sum(string[i:])
            scores.append(left + right)
        print(scores)
        return max(scores)

# Solution from leetcode
