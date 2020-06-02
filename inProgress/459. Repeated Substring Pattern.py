def repeatedSubstringPattern(s):
    for end in range(1, len(s)//2 +1):
        sub = s[:end]
        string = s
        string = string.replace(sub, "")
        if len(string) ==0:
            return True
    return False

# smallest solution on leetcode
def repeatedSubstringPatternSmall(s):
    return s in (s + s)[1: -1]

if __name__ == '__main__':
    s = "abab"
    s = "abcabcabc"
    print(repeatedSubstringPatternSmall(s))