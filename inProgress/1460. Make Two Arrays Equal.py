def canBeEqual(target, arr):
    if len(target) != len(arr):
        return False
    if len(set(target) - set(arr)) != len(set(arr) - set(target)):
        return False
    for index_t, value_t in enumerate(target):
        if target == arr:
            return True
        index_a = index_t
        for value_a in arr[index_t:]:
            if value_t == value_a:
                arr[index_t: index_a + 1] = arr[index_t: index_a + 1][::-1]
                break
            index_a += 1
        if target == arr:
            return True
    if target == arr:
        return True
    else: return False

# best solution on leetcode
def canBeEqualBest(target, arr):
    ans = 0
    for x, y in zip(target, arr):
        ans ^= x
        ans ^= y
    return ans == 0

# second best solution on leetcode
def canBeEqualBest2(target, arr):
    target.sort()
    arr.sort()
    if target == arr:
        return (True)
    else:
        return (False)


if __name__ == '__main__':
    # target = [1, 2, 3, 4]
    # arr = [2, 4, 1, 3]
    # target = [7]
    # arr = [7]
    # target = [1, 12]
    # arr = [12, 1]
    target = [937,396,309,316,278,305,937,563,385,816,333,523,874,47,281,984,431,692]
    arr = [937,385,816,937,309,523,281,278,316,396,984,431,47,333,692,874,563,305]
    print(canBeEqual(target, arr))
