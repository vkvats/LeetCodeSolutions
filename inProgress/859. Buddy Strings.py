def buddyStrings(A, B):
    if len(A) != len(B):
        return False
    elif sorted(A) != sorted(B):
        return False
    elif A == B and len(set(A)) == len(A):
        return False
    else:
        count = 0
        for i in range(len(A)):
            if A[i] != B[i]:
                count += 1
                if count == 3:
                    return False
        return True

# missed few cases in above question, took hint from dicussion

# best solution from leetcode
def buddyStringsBest(A, B):
    # if lengths are different, then must be false
    if len(A) != len(B):
        return False
    # If A and B are same, then A must have duplicate character
    if A == B:
        seen = set()
        for a in A:
            if a in seen:
                return True
            seen.add(a)
        return False

    pair = []
    # when A and B are not same
    for a, b in zip(A, B):
        if a != b:
            pair.append((a, b))
        if len(pair) > 2:
            return False

    return len(pair) == 2 and pair[0] == pair[1][::-1]



if __name__ == '__main__':
    A = "aa"
    B = "aa"
    # A = "aaaaaaabc"
    # B = "aaaaaaacb"
    # A= ""
    # B = "aa"
    # A= "ab"
    # B = "ab"
    A = "abcaa"
    B = "abcbb"
    print(buddyStrings(A,B))