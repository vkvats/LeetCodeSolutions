from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        common = count.most_common(k)
        output = []
        for (key, val) in common:
            output.append(key)
        return output

# Solution from leetcode
import heapq

class SolutionF1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dt = collections.Counter(nums)
        return heapq.nlargest(k, dt.keys(), key=lambda x:dt[x])

