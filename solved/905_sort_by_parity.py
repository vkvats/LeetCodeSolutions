# first thought
def sortArrayByParity(A):
    even =[]
    odd =[]
    [even.append(x) if x%2 ==0 else odd.append(x) for x in A]
    even.extend(odd)
    return even

# from discussion
def sortArrayByParityD(A):
    # A key can be used to specify sorting criteria
    A.sort(key=lambda x: x % 2)
    return A

# Sorting with different keys
def keyFirstSort(A):
    A.sort(key = lambda x:x % 4)
    return A

if __name__ == '__main__':
    A = [3,1,2,4]
    print(sortArrayByParityD(A))
    print(oddFirstSort(A))