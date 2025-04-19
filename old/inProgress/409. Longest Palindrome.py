# making it faster in order N
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        freq = {}
        length = 0
        for key in s:
            val = freq.get(key, 0) + 1
            freq[key] = val
            if val % 2 == 0:
                length += val
                freq[key] = 0
        return length + 1 if any(freq.values()) else length


# First solution
from collections import Counter
class Solutionf:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        length = 0
        for key, val in freq.items():
            if val % 2 == 0:
                length += val
                freq[key] = 0
            else:
                new_val = val - 1
                length += new_val
                freq[key] = 1
        return length + 1 if any(freq.values()) else length


if __name__ == '__main__':
    s = "ba"
    print(Solution().longestPalindrome(s))