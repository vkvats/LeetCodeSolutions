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

