def primeFactors(n):
    number = n
    import math
    prime_factors = []
    while n % 2 == 0:
        n = n / 2
        prime_factors.append(2)

    for i in range(3, number +1, 2):
        while n % i == 0:
            n = n / i
            prime_factors.append(i)
    return prime_factors

if __name__ == '__main__':
    n = 14
    print(primeFactors(n))