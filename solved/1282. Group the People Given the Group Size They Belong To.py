class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        output = []
        n = len(groupSizes)
        groups_n = [(n, group) for n, group in zip(range(n), groupSizes)]
        groups_n.sort(key = lambda x: x[1])
        i = 0
        while i < n:
            val, size = groups_n[i]
            tmp = []
            for v, _ in groups_n[i : i + size]:
                tmp.append(v)
            i += size
            output.append(tmp)

# Solution from leetcode
sample 64 ms submission
import collections

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = collections.defaultdict(list)
        for i in range(len(groupSizes)):
            d[groupSizes[i]].append(i)
        lst = []
        for k in d.keys():
            lst += (d[k][i:i+k] for i in range(0, len(d[k]), k))
        return lst

# Solution from leetcode
