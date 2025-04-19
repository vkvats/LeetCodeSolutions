# new method
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS = Counter(s)
        hashT = Counter(t)
        return True if hashS == hashT else False


def isAnagram(s,t):
    listS = list(s)
    for alpha in t:
        if alpha in listS:
            listS.remove(alpha)
        else:
            return False
    if len(listS) == 0:
        return True
    else:
        return False

def isAnagramHash(s,t):
    hashS = {}
    hashT = {}
    for x in s:
        hashS[x] = hashS.get(x,0)+1
    for y in t:
        hashT[y] = hashT.get(y,0)+1
    if hashS == hashT:
        return True
    else: return False

# best solution of leetcode
from collections import Counter
def isAnagramBest(s,t):
    countsS = Counter(s)
    countsT = Counter(t)
    if countsS != countsT:
        return False

    return True
if __name__ == '__main__':
    s = 'catttt'
    t = "cat"
    print(isAnagramHash(s,t))