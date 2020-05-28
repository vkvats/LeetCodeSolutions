# first thought
def sortedSquares(A):
    return sorted([x**2 for x in A])

if __name__ == '__main__':
    A = [-4,-1,0,3,10]
    print(sortedSquares(A))