def minStartValue(nums):
    start_value = []
    total_sum = 0
    for num in nums:
        total_sum = total_sum + num
        start_value.append(total_sum)
    min_value = min(start_value)
    if min_value >=0:
        return 1
    else:
        return abs(min_value) + 1

def minStartValue2(nums):
    # start_value = []
    min_value = None
    total_sum = 0
    flag = True
    for num in nums:
        total_sum = total_sum + num
        if flag:
            min_value = num
            flag = False
        if total_sum < min_value:
            min_value = total_sum
    if min_value >=0:
        return 1
    else:
        return -min_value + 1

if __name__ == '__main__':
    nums = [-3, 2, -3, 4, 2]
    # nums = [1, 2]
    # nums = [1, -2, -3]
    print(minStartValue2(nums))