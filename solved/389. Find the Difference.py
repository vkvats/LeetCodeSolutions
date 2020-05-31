def findTheDifference(s, t):
    listT = list(t)
    for alpha in s:
        if alpha in listT:
            listT.remove(alpha)
    return listT[0]

# best solution of leetcode
from collections import Counter

def findTheDifferenceBest(s, t):

    if set(s) != set(t):
        return (set(t) - set(s)).pop()

    else:
        s = Counter(s)
        t = Counter(t)
        for i, j in s.items():
            if j != t[i]:
                return i

if __name__ == '__main__':
    s = "ae"
    t = "aea"
    print(findTheDifference(s,t))
