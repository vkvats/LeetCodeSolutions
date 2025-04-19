def firstUniqChar(s):
    count = {}
    for alpha in s:
        count[alpha] = count.get(alpha, 0) + 1
    for index, alpha in enumerate(s):
        if count[alpha]==1:
            return index
    return -1

# best soution on leetcode
from collections import Counter
def firstUniqCharBest(s):
    fc = len(s)
    # something is missing
    for c in string.ascii_lowercase:
        left = s.find(c)
        if left != -1 and left == s.rfind(c):
            fc = min(left, fc)
    return fc if fc != len(s) else -1
if __name__ == '__main__':
    s = "leetcode"
    s = "loveleetcode"
    print(firstUniqChar(s))