def largestSumAfterKNegations(A, K):
    A.sort()
    left = K
    for i in range(K):
        if A[i] <0:
            A[i] = -A[i]
            left -= 1
    if left % 2 ==0:
        return sum(A)
    else:
        A.sort()
        A[0] = -A[0]
        return sum(A)

# best solution from Leetcode
def largestSumAfterKNegationsFast(A,K):
    A, ncnt = sorted(A), sum([1 for a in A if a < 0])
    cnt1, cnt2 = min(K, ncnt), K - ncnt if K > ncnt else 0
    for i in range(cnt1):
        A[i] = - A[i]
    return sum(A) - min(A) * 2 * (cnt2 % 2) if cnt2 else sum(A)

if __name__ == '__main__':
    # A = [4, 2, 3]
    # K = 1
    # A = [3, -1, 0, 2]
    # K = 3
    A = [2, -3, -1, 5, -4]
    K = 3
    print(largestSumAfterKNegations(A, K))