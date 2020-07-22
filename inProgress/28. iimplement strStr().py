class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            index = haystack.index(needle)
        except ValueError:
            return -1
        return index


# Solution from leetcode
class SolutionF1:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        lenHay = len(haystack)
        n = len(needle)
        for i in range(lenHay):
            end = i+n
            if end < lenHay+1:
                compStr = haystack[i:end]
                if compStr == needle:
                    return i
            else: return -1
        return -1

# Solution from leetcode
class SolutionF2:
    def strStr(self, haystack: str, needle: str) -> int:
        dic = {}
        if len(haystack) - len(needle) == 0 and haystack == needle: return 0
        for i in range(len(haystack) - len(needle) + 1):
            dic[haystack[i:i+len(needle)]] = 1
            if needle in dic: return i
        return -1