def sortString(s):
    from collections import Counter
    result = ""
    n = len(s)
    i = 0
    unique = sorted(set(s))
    while i < n:
        for alpha in unique:
            if alpha in s:
                result += alpha
                s = s.replace(alpha, '', 1)
                i += 1
        for alpha2 in unique[::-1]:
            if alpha2 in s:
                result += alpha2
                s = s.replace(alpha2, '', 1)
                i += 1

    return result

if __name__ == '__main__':
    s = "spo" #"gggggg" #"leetcode" # "ddddaaaabbbbcccc"
    print(sortString(s))