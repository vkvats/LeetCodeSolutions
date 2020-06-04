def countPrimes(n):
    import math
    def primeNumbers(a):
        if a ==1:
            return False
        if a ==2:
            return True
        if a> 2 and a %2 ==0:
            return False
        max_divisor = math.floor(math.sqrt(a))
        for d in range(3, 1+max_divisor, 2):
            if a % d ==0:
                return False
        return True
    # main function
    count =[]
    for i in range(1, n):
        if primeNumbers(i):
            count.append(i)
    return count

if __name__ == '__main__':
    n = 10# 499979  # failure cases ( 2,
    print(countPrimes(n))


###
# def primeNumbers(a):
#     if a ==1:
#         return False
#     max_divisor = math.floor(math.sqrt(n))
#     for d in range(2, 1+ max_divisor):
#         if n % d ==0:
#             return False
#     return True