# new solution
# in one pass
class Solution:
    def isMonotonic(self, A: [int]) -> bool:
        n = len(A)
        if n == 1: return True
        first, second = 0,1
        while A[first] == A[second]: # first break the condition of equality
            second += 1
            if second == n: return True # if all elements are equal return True
        first_num, second_num = A[first], A[second]
        if first_num > second_num: # decreasing Condition should be applied
            for i in range(second, n):
                if A[i] > A[i-1]: return False
            else: return True
        elif first_num < second_num: # increasing Condition should be applied
            for i in range(second, n):
                if A[i] < A[i-1]: return False
            else: return True



def isMonotonic(A):
    nonDecreasing = True
    nonIncreasing = True

    for index in range(1, len(A)):
        if not (A[index] <= A[index-1]):
            nonIncreasing = False
        elif not (A[index] >= A[index-1]):
            nonDecreasing = False
    if not nonIncreasing and nonDecreasing :
        return True
    elif nonIncreasing and not nonDecreasing:
        return True
    elif nonIncreasing and nonIncreasing:
        return True
    else: return False

# best solution 460 ms
def isMonotonic( A):
    if A[0] <= A[-1]:
        A = A[::-1]
    # Expected A is decreasing order
    for i in range(1, len(A)):
        if A[i - 1] < A[i]:
            return False

    return True

if __name__ == '__main__':
    # A = [1,2,2,3]
    # A= [6,5,4,4]
    # A = [1,3,2]
    # A= [1,2,4,5]
    A= [1,1,1]
    print(isMonotonic(A))

