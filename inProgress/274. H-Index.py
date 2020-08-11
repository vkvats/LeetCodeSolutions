class Solution:
    def hIndex(self, citations: [int]) -> int:
        if not citations: return 0
        n = len(citations)
        if sum(citations) == 0 : return 0
        if n == 1: return 1
        citations.sort()
        for cite in range(len(citations), -1, -1):
            if citations[n-cite] >= cite:
                return cite