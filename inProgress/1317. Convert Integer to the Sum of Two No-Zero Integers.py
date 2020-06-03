def getNoZeroIntegers(n):
    for first_num in range(1,n):
        if "0" not in str(first_num) and "0" not in str(n- first_num):
            return [first_num,n-first_num]

if __name__ == '__main__':
    n = 4102
    print(getNoZeroIntegers(n))