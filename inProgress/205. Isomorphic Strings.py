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
