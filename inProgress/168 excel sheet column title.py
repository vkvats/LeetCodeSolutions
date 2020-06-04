def convertToTitle(n):
    # This string collects the letters for the column title.
    col_title = ''

    # While n > 0, the next letter is the letter at (n - 1) % 26. Then n = (n - 1) // 26
    while n > 0:
        # 65 is the ASCII value for 'A'
        col_title += chr(65 + (n - 1) % 26)
        n = (n - 1) // 26
    return col_title[::-1]

# best method on leetcode
def convertToTitleBest(n):
    ret = []
    while n:
        ret.append(chr((n - 1) % 26 + 65))
        n = (n - 1) // 26
    return "".join(reversed(ret))

# more clear solution
def convertToTitleClear(n):
    if n < 1:
        return ''
    result = ''
    l = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while n:
        n -= 1
        r = n % 26
        result = l[r] + result
        n = n // 26
    return result



if __name__ == '__main__':
    n = 701
    print(convertToTitle(n))