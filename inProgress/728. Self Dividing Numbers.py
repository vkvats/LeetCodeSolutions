def selfDividingNumbers(left, right):
    output =[]
    for num in range(left, right + 1):
        flag = True
        digit_list = list(map(int, list(str(num))))
        if 0 not in digit_list:
            for digit in digit_list:
                if not num % digit ==0:
                    flag = False
                    break
            if flag:
                output.append(num)
    return output
## some good solutions from leetcode
def selfDividingNumbers1(left, right):

    def self_dividing(num):
        n = num
        while n > 0:
            i = n % 10
            if i == 0 or num % i != 0: return False
            n //= 10

        return True

    return [n for n in range(left, right + 1) if self_dividing(n)]

# another good solution
def selfDividingNumbers2(left, right):
    res = []
    for i in range(left, right + 1):
        num = i
        while num:
            if (num % 10) and i % (num % 10) == 0:
                num //= 10
            else:
                break
        if num == 0:
            res.append(i)
    return res

if __name__ == '__main__':
    left = 1
    right = 22
    print(selfDividingNumbers(left, right))