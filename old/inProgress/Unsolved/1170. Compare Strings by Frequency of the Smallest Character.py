class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        words_f = []
        for w in words:
            smallest_w = sorted(w)[0]
            count = w.count(smallest_w)
            words_f.append(count)
        output = []
        for q in queries:
            smallest_q = sorted(q)[0]
            q_count = q.count(smallest_q)
            condition_count = 0
            for w_count in words_f:
                if q_count < w_count:
                    condition_count += 1
            output.append(condition_count)
        return output

# Solution from leetcode
import bisect
class SolutionF1:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        f = sorted(w.count(min(w)) for w in words)
        return [len(f) - bisect.bisect(f, q.count(min(q))) for q in queries]