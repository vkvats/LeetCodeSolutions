def maximum69Number(num):
    nums = list(str(num))
    for index, n in enumerate(nums):
        if n != "9":
            nums.remove(n)
            nums.insert(index, "9")
            break
    return "".join(nums), type("".join(nums))

# good solutions on leetcode
def maximum69Number1(num):
    """We can use the replace method from string to replace the first 6 to 9
    str.replace() do not reutrn error if it finds nothing"""
    return int(str(num).replace('6', '9', 1))


if __name__ == '__main__':
    num = 9669
    num = 696
    print(maximum69Number(num))