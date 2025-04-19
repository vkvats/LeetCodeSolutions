def buildArray(target, n):
    arr = []
    arr_el = []
    for a in range(1, n+1):
        if a in target:
            arr.append("Push")
            arr_el.append(a)
        else:
            arr.append("Push")
            arr.append("Pop")
        if arr_el == target:
            break
    return arr

## best solution from leetcode
def buildArrayBest(target, n):
    ans = []
    for i in range(1, n + 1):
        if i in target:
            ans.append("Push")
            target.remove(i)
        else:
            ans.append("Push")
            ans.append("Pop")
        if not target:
            return ans
    return ans


if __name__ == '__main__':
    # target = [1, 3]
    # n = 3
    # target = [1, 2, 3]
    # n = 3
    target = [1,2] # push push
    n = 4
    print(buildArray(target, n))
    # print(target == [1,2])