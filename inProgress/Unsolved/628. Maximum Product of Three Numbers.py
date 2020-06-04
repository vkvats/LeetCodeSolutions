def maximumProduct(nums):
    arr = sorted(nums)
    if arr[0] >=0:
        a, b, c= arr[-1], arr[-2], arr[-3]
        return a*b*c
    elif arr[0] <0:
        a = max(abs(arr[0]), arr[-1])
        if a == abs(arr[0]):
            b = max(abs(arr[1]), arr[-1])
            if b == abs(arr[1]):
                pass
        c = max(abs(arr[2]), arr[-3])
        return a*b*c


if __name__ == '__main__':
    nums = [-4,-5,6,1,2,3]
    print(maximumProduct(nums))