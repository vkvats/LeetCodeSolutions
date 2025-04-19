def addStrings(num1, num2):

    def convert(number):
        str_to_num = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        base = 10
        num = 0
        index = 0
        for str_num in reversed(number):
            num += base**index * str_to_num[str_num]
            index +=1
        return num
    return convert(num1) + convert(num2)

if __name__ == '__main__':
    num1 = "100002"
    num2 = "10837485"
    print(addStrings(num1, num2))
    print(int(num1) + int(num2))