def maxPower(s):
    powers =[]
    string = ""
    s = s + "-"
    for alpha in s:
        if len(string)==0:
            string = string + alpha
        elif alpha in string and len(string) !=0:
            string = string + alpha
        elif alpha not in string and len(string) != 0:
            powers.append(len(string))
            string = alpha
    return max(powers)

# best solution from leetcode
def maxPowerBest(s):
    l = 1
    res = 1
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            l += 1
            res = max(res, l)
        else:
            l = 1
    return res

if __name__ == '__main__':
    s = "leetcode"
    s = "abbcccddddeeeeedcba"
    s = "triplepillooooow"
    s = "hooraaaaaaaaaaay"
    # s = "tourist"
    # s = "cc"
    print(maxPower(s))