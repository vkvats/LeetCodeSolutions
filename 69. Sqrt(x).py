def mysqrt( x):
    if x < 2:
        return x
    start = 1
    end = x

    while start < end:
        mid_num = start + (end - start) // 2
        if mid_num * mid_num == x:
            return mid_num
        elif mid_num * mid_num > x:
            end = mid_num
        elif mid_num * mid_num < x:
            start = mid_num + 1
    return start - 1
