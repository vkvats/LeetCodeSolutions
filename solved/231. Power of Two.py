def isPowerOfTwo(n):
    if n ==0:
        return False
    while n%2==0:
        n = n/2
    if n==1:
        return True
    else:
        return False

# Solution from leet code
def isPowerOfTwoBest (n):
    return n > 0 and n & (n - 1) == 0



if __name__ == '__main__':
    n = 218
    print(isPowerOfTwo(n))