def removeDuplicates(S):
    """using string method"""
    flag = True
    def duplicateCheck(string):
        for i in range(1, len(string)):
            if string[i] == string[i-1]:
                return True, string[i]
        return False, None

    while flag:
        flag, alpha = duplicateCheck(S)
        if flag == False:
            break
        S = S.replace(alpha+alpha, "", 1)
    return S

# second best solution
def removeDuplicates2(S):
    doubles = {'aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq',
               'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz'}

    while True:
        count = 0
        for double in doubles:
            if double in S:
                S = S.replace(double, "")
                count += 1
        if count == 0:
            break
    return S

# best solution
def removeDuplicates1(S):  # O(N), O(N-D) D is total length of duplicates
    output = []
    for ch in S:
        if output and ch == output[-1]:
            output.pop()
        else:
            output.append(ch)
    return ''.join(output)


from string import ascii_lowercase
def removeDuplicates3(S):
    # generate 26 possible duplicates
    duplicates = {2 * ch for ch in ascii_lowercase}
    prev_length = -1
    while prev_length != len(S):
        prev_length = len(S)
        for d in duplicates:
            S = S.replace(d, '')
    return S

if __name__ =='__main__':
    S = "abbaca"
    print(removeDuplicates(S))
