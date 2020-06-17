def isSubsequence(s, t):
    index = 0
    for alpha in s:
        if index < len(t):
            present = t.find(alpha, index, len(t))
            if present == -1:
                return False
            index = present + 1
        else:
            return False
    return True

# fastest solution on leetcode
def isSubsequenceFast(s, t):
    s_len, t_len = len(s), len(t)
    #if s_len == t_len == 0:
    #    return True

    i, j = 0, 0

    while i < s_len and j < t_len:
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == s_len
# second fastest solution on leetcode
def isSubsequenceFast2(s, t):
    if s == "":
        return True
    if t == "":
        return False

    j = 0
    for i in range(len(t)):

        if s[j] == t[i]:
            j += 1
            if j == len(s):
                return True

    return False

if __name__ == '__main__':
    s = "abc"
    t = "ahbgdc"
    # s = "axc"
    # t = "ahbgdc"
    # s = "acb"
    # t = "ahbgdc"
    # s = "aaaaaa"
    # t = "bbaaaa"
    print(isSubsequence(s,t))