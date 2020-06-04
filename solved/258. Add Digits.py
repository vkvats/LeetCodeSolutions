def addDigits(num):
    if num == 0:
        return 0
    else :
        return 1 + (num-1) % 9


# best solution on leetcode
def addDigitsBest(num):
    return num - 9 * int((num - 1) / 9)


if __name__ == '__main__':
    num = 38
    print(addDigits(num))