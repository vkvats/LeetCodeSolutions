def reverseString(s):
    for i in range(len(s)):
        s.insert(i,s.pop())
    return s

## othe mewthod
s[::-1]
s.reverse()


if __name__ == '__main__':
    s = ["h","e","l","l","o"]
    print(s[::-1])
    print(reverseString(s))
