def largestPerimeter(A):
    A = sorted(A) # sorting will only help to find max perimeter, but it wont find all combinations.
    valid_triangles = {}
    for index in range(len(A)-2):
        a, b, c = A[index], A[index+1], A[index+2]
        if a+b>c and b+c>a and a+c>b:
            valid_triangles[(a,b,c)] = a+b+c
    if len(valid_triangles)==0:
        return 0
    else:
        max_perimeter = max(valid_triangles.values())
        return max_perimeter

# Best solution on leetcode
def largestPerimeterBest(A):
    A.sort()

    b = len(A) - 1
    m = b - 1
    s = b - 2

    while b >= 2:
        if A[m] + A[s] > A[b]:
            return A[m] + A[s] + A[b]
        b = m
        m = s
        s = b - 2

    return 0

## same technique but it will give faster result due to reversing the order of list.
def largestPerimeterFast(A):
    A.sort(reverse=True)
    for i in range(len(A) - 2):
        if A[i] < A[i + 1] + A[i + 2]:
            return A[i] + A[i + 1] + A[i + 2]
    return 0

if __name__ == '__main__':
    A = [3,2,3,4]
    A= [1,2,1]
    print(largestPerimeter(A))

