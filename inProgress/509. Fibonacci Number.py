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

# recursion solution
def fibR(N):
    if N == 0:
        return 0
    if N == 1:
        return 1
    return fibR(N-1) + fibR(N-2)

if __name__ == '__main__':
    N = 10
    print(fib(N))

