def trailingZeroes(n):
    zeros = 0
    if n ==0:
        return 0
    flag = True
    divisor = 5
    power = 1
    while divisor**power <= n:
        count = n/ (divisor**power)
        power +=1
        zeros += int(count)
    return zeros

# best solution on leetcode
"""Same thought"""
def trailingZeroesBest(n):
    k = 1
    zeros = 0
    while 5 ** k <= n:
        zeros += n // (5 ** k)
        k += 1
    return zeros

if __name__ == '__main__':
    n = 30
    print(trailingZeroesBest(n))