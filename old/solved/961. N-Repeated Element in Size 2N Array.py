# new solution
# using hashing
class Solution:
    def repeatedNTimes(self, A: [int]) -> int:
        count = set()
        for num in A:
            # as per question, only one number is repeated N times
            # rest of the numbers are unique.
            if num in count: return num
            else: count.add(num)

# using random sampling
import random
def repeatedNTimes(self, A):
    while 1:
        # take out 2 samples from array, if they are same, return them
        s = random.sample(A, 2)
        if s[0] == s[1]:
            return s[0]

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