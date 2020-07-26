class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = [i for i in range(1, m + 1)]
        output = []
        for q in queries:
            idx_q = p.index(q)
            output.append(idx_q)
            p.remove(q)
            p.insert(0, q)
        return output
# solution from leetcode
class SolutionF1:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        l=[i for i in range(1,m+1)]
        ans=[]
        for i in queries:
            ind=l.index(i)
            ans.append(ind)
            l.pop(ind) # we can use pop with any index
            l.insert(0,i)
        return ans