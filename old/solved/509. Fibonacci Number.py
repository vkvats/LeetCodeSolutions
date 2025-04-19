# New method
# recursive solution with memoization
class Solution:
    def fib(self, N: int) -> int:
        fib_num = {}

        def recurse(n):
            if n in fib_num: return fib_num[n]
            if n < 2:
                return n
            else:
                fib_n = recurse(n - 1) + recurse(n - 2)
            fib_num[n] = fib_n
            return fib_n

        return recurse(N)

# recursion solution
def fibR(N):
    if N == 0:
        return 0
    if N == 1:
        return 1
    return fibR(N-1) + fibR(N-2)


# using decorators 
from functools import lru_cache
class Solution:
    @lru_cache(maxsize=None)
    def fib(self, n: int) -> int:
        if n < 2: return n
        return self.fib(n-1) + self.fib(n-2)

# Iterative solution
def fib(N):
    fib_num = {1: 0, 2: 1}
    if N == 0:
        return 0
    elif N == 1:
        return 1
    elif N == 2:
        return 1
    for i in range(3, N + 1):
        new_fib_num = fib_num[i - 1] + fib_num[i - 2]
        fib_num[i] = new_fib_num
    return fib_num[N] + fib_num[N - 1]



if __name__ == '__main__':
    N = 10
    print(fib(N))

