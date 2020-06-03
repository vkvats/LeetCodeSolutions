def titleToNumber(s):
    output = 0
    for index, alpha in enumerate(s[::-1]):
        output += 26 ** index * (ord(alpha) - 64)
    return output

if __name__ == '__main__':
    s = "ZY"
    print(titleToNumber(s))