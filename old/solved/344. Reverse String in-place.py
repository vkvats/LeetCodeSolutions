# New method
# using recursion and inplace
def reverseString(s):
    def helper(left, right):
        if left < right:
            s[left], s[right] = s[right], s[left]
            helper(left + 1, right - 1)
    helper(0, len(s)-1)

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
