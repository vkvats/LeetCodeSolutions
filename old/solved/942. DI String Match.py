def diStringMatch(S):
    arr = list(range(len(S)+1))
    output = []
    for alpha in S:
        if alpha =="I":
            output.append(arr.pop(0))
        else:
            output.append(arr.pop())
    output.append(arr.pop())
    return output

# Some good solutions from leetcode
"""Same thought, faster implementation"""
def diStringMatch1(self, S: str) -> List[int]:
    lo, hi = 0, len(S)
    ans = []
    for x in S:
        if x == 'I':
            ans.append(lo)
            lo += 1
        else:
            ans.append(hi)
            hi -= 1

    return ans + [lo]

"""Different line of thought """
def diStringMatch2(self, S: str) -> List[int]:
    d = S.count("D")
    i = S.count("I")

    down = d - 1
    up = d + 1

    res = [0] * (len(S) + 1)
    res[0] = d

    for i in range(len(S)):
        if S[i] == "D":
            res[i + 1] = down
            down -= 1
        else:
            res[i + 1] = up
            up += 1
    return res





if __name__ == '__main__':
    S= "IDID"
    S = "III"
    S = "DDI"
    print(diStringMatch(S))