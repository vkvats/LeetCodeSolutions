import numpy as np

def longest_common_subsequence(string1, string2):
    n1, n2 = len(string1), len(string2)
    # split the string into each characters
    string1 = list(string1)
    string2 = list(string2)
    # insert zero before both strings
    string1.insert(0,0)
    string2.insert(0,0)
    table = np.zeros((n1 + 1, n2 + 1))
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if string1[i] == string2[j]:
                table[i,j] = 1 + table[i-1, j-1]
            else:
                table[i,j] = max(table[i-1, j], table[i, j-1])
    return table[n1,n2]

def longestCommonSubsequence(text1, text2):
        memo = collections.defaultdict(list)
        for i, a in enumerate(text1):
            memo[a].append(i)
        tmp = []
        for c in text2:
            tmp += memo[c][::-1]
            
        # print(tmp)
        def lis(arr):
            dp = [-1]
            for n in arr:
                if n > dp[-1]:
                    dp.append(n)
                else:
                    idx = bisect.bisect_left(dp, n)
                    dp[idx] = n
            return len(dp) - 1
        return lis(tmp)

if __name__ == '__main__':
    string1 = "bsbininm"
    string2 = "jmjkbkjkv"
    print(longest_common_subsequence(string1, string2))