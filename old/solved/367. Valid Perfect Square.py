def perfectSquare( num):
    if num == 1:
        return True
    if num < 1:
        return False
    if num % 10 not in (1, 4, 5, 6, 9, 0):
        return False
    # now will do binary search.
    start = 1
    end = num
    while start <= end:
        mid_num = start + (end - start)//2
        if mid_num * mid_num == num:
            return True
        elif mid_num * mid_num > num:
            end = mid_num - 1
        elif mid_num * mid_num < num:
            start = mid_num + 1
    return False

