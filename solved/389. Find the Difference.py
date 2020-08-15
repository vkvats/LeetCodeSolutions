# new method
# using sorting the text and then comparing chars
import collections
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)
        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]
        else: return t[-1]

# using bit manipulation
class Solution:
    # SOR with same number gives zero. so only the extra
    # number will be left at the end.
    def findTheDifference(self, s: str, t: str) -> str:
        bit = ord(t[0])
        for char in t[1:] + s:
            bit ^= ord(char)
        return chr(bit)
# bit manipulation
import operator
from functools import reduce

class Solution():
    def findTheDifference(self, s, t):
        return chr(reduce(operator.xor, map(ord, s + t)))

# using ORD function
class Solution(object):
    """
    difference
    """
    def findTheDifference(self, s, t):
        diff = 0
        for i in range(len(s)):
            diff -= ord(s[i])
            diff += ord(t[i])
        diff += ord(t[-1])
        return chr(diff)

# using dictionary difference
class Solution(object):
    def findTheDifference(self, s, t):
        """
        dictionary difference gives the difference in keys, it doesn't care about values of the keys
        """
        return list((collections.Counter(t) - collections.Counter(s)))[0]

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
