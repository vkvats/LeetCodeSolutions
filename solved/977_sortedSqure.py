import time
# first thought
def sortedSquares(A):
    # return sorted([x**2 for x in A])
    return sorted([x*x for x in A]) # faster than X**2
    # return sorted(x*x for x in A) # dont need to cast in list

if __name__ == '__main__':
    A = [x for x in range(10000000)]
    tic = time.time()
    _ = sortedSquares(A)
    toc = time.time() - tic
    print(toc)