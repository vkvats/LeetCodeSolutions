from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(sorted(words)) # words had to be in sorted order
        common = count.most_common(k)
        output = []
        for (key, val) in common:
            output.append(key)
        return output