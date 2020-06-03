def subtractProductAndSum(n):
    product = 1
    sum = 0
    # n = n //10
    for i in range(len(str(n))-1):
        num = n%10
        n = n//10
        product *= num
        sum += num
    product *= n
    sum += n
    return product - sum

# best solution from leetcode
"""I also thought about using strings and iterating over, but then i thought to use maths to do the same."""
def subtractProductAndSumBest(self, n=234):
    a = 0
    x = []
    for i in str(n):
        a = i
        x.append(a)
    for i in range(0, len(x)):
        if i == 0:
            s = int(x[0])
            p = int(x[0])
        else:
            s = s + int(x[i])
            p = p * int(x[i])
    return p - s

# second best solution from leetcode
def subtractProductAndSumSB(n):

    n = list(map(int, list(str(n))))
    product = 1
    for x in n:
        product *= x

    Sum = sum(n)
    return product - Sum

if __name__ == '__main__':
    n = 4421
    print(subtractProductAndSumSB(n))