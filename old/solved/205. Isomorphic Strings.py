# new solution
# Using ZIP (but slower than dictionary)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = dict(zip(s,t))
        mapping2 = dict(zip(t,s))
        for c1, c2 in zip(s,t):
            if mapping[c1] != c2 or mapping2[c2] != c1: return False
        else: return True

# Using ZIP in different manner
def isIsomorphic(self, s, t):
    """The length of both way zip should be same"""
    return len(set(zip(s, t))) == len(set(s)) and len(set(zip(t, s))) == len(set(t))

def isIsomorphic(s, t):
    mapping = {}
    for index in range(len(s)):
        if s[index] in mapping:
            if mapping[s[index]]!= t[index]  :
                return False
        else:
            if t[index] not in mapping.values():
                mapping[s[index]] = t[index]
            else:
                return False
    return True

# best leetcode solution
def isIsomorphicBest(s, t):
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))

if __name__ == '__main__':
    # s = "aba"
    # t = "baa"
    # s = "egg"
    # t = "add"
    # s = "foo"
    # t = "bar"
    # s = "paper"
    # t = "title"
    # s= "a"
    # t = "a"
    s = "ab"
    t = "aa"
    print(isIsomorphic(s,t))
