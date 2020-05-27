# first thought
def sumZero(n):
    arr =[]
    if n % 2 !=0:
        num = -1* (n//2)
        for i in range(n):
            arr.append(num)
            num +=1
    else:
        num = -1*(n//2)
        for i in range(n):
            if num ==0:
                num +=1
            arr.append(num)
            num +=1
    return arr, sum(arr)

# from dicussion
"""Can think of adding 0 if n is even and then do the same """


if __name__ == '__main__':
    n = 6
    print(sumZero(n))
