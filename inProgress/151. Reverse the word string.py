class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words = [w.strip() for w in words]
        i, j = 0, len(words) - 1
        while i < j:
            words[i], words[j] = words[j], words[i]
            i += 1
            j -= 1
        s = " ".join(words)
        return s

# solution from leetcode
class SolutionF1:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])

if __name__  == '__main__':
    s = " hello   world  "
    print(Solution().reverseWords(s))