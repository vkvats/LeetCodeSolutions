class Solution:
    def findAndReplacePattern(self, words: [str], pattern: str) -> [str]:
        output = []
        for word in words:
            mapping = {}
            rev_map = {}
            flag = True
            for p, w in zip(pattern, word):
                if p in mapping:
                    if mapping[p] != w:
                        flag = False
                        break
                else:
                    mapping[p] = w
                if w in rev_map:
                    if rev_map[w] != p:
                        flag = False
                        break
                else:
                    rev_map[w] = p
            if flag:
                output.append(word)
        return output

# Solution from leetcode
class SolutionF1:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        d = []
        ppttrn = []
        for c in pattern:
            if c not in d:
                pos = len(d)
                d.append(c)
                ppttrn.append(pos)
            else:
                pos = d.index(c)
                ppttrn.append(pos)
        sol = []
        for w in words:
            d = []
            pttrn = []
            for c in w:
                if c not in d:
                    pos = len(d)
                    d.append(c)
                    pttrn.append(pos)
                else:
                    pos = d.index(c)
                    pttrn.append(pos)
            if pttrn == ppttrn:
                sol.append(w)

        return sol

# solution from leetcode
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        listy = []
        for x in words:
            temp1 = x.translate(x.maketrans(x, pattern))
            if temp1 != pattern:
                continue
            temp2 = temp1.translate(temp1.maketrans(pattern, x))
            if x == temp2:
                listy.append(x)

        return listy
        temp = {x for x in words if x.translate(x.maketrans(x, pattern)).maketrans(pattern, x) == x}
        return temp


if __name__ == '__main__':
    words = ["abc","deq","mee","aqq","dkd","ccc"]
    pattern = "abb"
    print(Solution().findAndReplacePattern(words, pattern))