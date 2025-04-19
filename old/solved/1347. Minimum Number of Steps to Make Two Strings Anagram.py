from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)
        count = 0
        for key, val_t in count_t.items():
            if key in count_s:
                val_s = count_s[key]
                count += min(val_s, val_t)
        return len(s) - count

# solution from leetcode
class SolutionF1:
    def minSteps(self, s: str, t: str) -> int:
        ret = 0
        for ch in set(s):
            diff = s.count(ch) - t.count(ch)
            ret += (diff if diff > 0 else 0)
        return ret

# solution from leetcode
