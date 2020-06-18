def maxProduct(nums):
    nums.sort()
    a,b = nums[-2:]
    return (a-1)*(b-1)

if __name__ == '__main__':
    # nums = [3, 4, 5, 2]
    # nums = [1, 5, 4, 5]
    nums = [3,7]
    print(maxProduct(nums))