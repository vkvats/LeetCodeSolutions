# New method
# using bisect function from bisect module
import bisect
class Solution:
    def numSmallerByFrequency(self, queries: [str], words: [str]) -> [int]:
        f = sorted(w.count(min(w)) for w in words)
        return [len(f) - bisect.bisect(f, q.count(min(q))) for q in queries]

    # same as above solution
    class Solution:
        def numSmallerByFrequency(self, queries: [str], words: [str]) -> [int]:
            words_f = sorted(w.count(min(w)) for w in words)
            len_w = len(words_f)
            output = []
            for q in queries:
                q_count = q.count(min(q))
                output.append(len_w - bisect.bisect(words_f, q_count))
            return output


# Old solution
class Solution:
    def numSmallerByFrequency(self, queries: [str], words: [str]) -> [int]:
        words_f = []
        for w in words:
            words_f.append(w.count(min(w)))
        output = []
        for q in queries:
            q_count = q.count(min(q))
            condition_count = 0
            for w_count in words_f:
                if q_count < w_count:
                    condition_count += 1
            output.append(condition_count)
        return output
