def repeatedNTimes(A):
    freq = {}
    for num in A:
        freq[num] = freq.get(num, 0) + 1
    N = len(A)//2
    for key, value in freq.items():
        if value == N:
            return key

def repeatedNTimesCounter(A):
    from collections import Counter
    freq = Counter(A)
    return freq.most_common()
# best solution from leetcode
def repeatedNTimesBest(A):
    for k in range(1, 3):
        for i in range(len(A) - k):
            if A[i] == A[i + k]:
                return A[i]
    return A[0]
if __name__ == '__main__':
    A = [1,2,3,3]
    A= [2,1,2,5,3,2]
    print(repeatedNTimes(A))