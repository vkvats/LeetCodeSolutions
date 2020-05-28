# First thought
def findTheDistanceValue(arr1, arr2, d):

    count = 0
    for a1 in arr1:
        flag = []
        for a2 in arr2:
            if abs(a1-a2) > d:
                flag.append(0)
            else:
                flag.append(1)
        if sum(flag) ==0:
            count +=1

    return count

# Other solutions
def FindTheDistanceValueLC(arr1, arr2, d):
    flag = [[0 if abs(a1 - a2) > d else 1 for a2 in arr2] for a1 in arr1]
    return sum([1 if sum(row) == 0 else 0 for row in flag])


# from discussion
def findTheDistanceValueFD(arr1, arr2, d):
    return sum([sum([abs(i - j) > d for i in arr2]) == len(arr2) for j in arr1])


if __name__ == '__main__':
    # arr1 = [4, 5, 8]
    # arr2 = [10, 9, 1, 8]
    # d = 2
    # arr1 = [1, 4, 2, 3]
    # arr2 = [-4, -3, 6, 10, 20, 30]
    # d = 3
    arr1 = [2, 1, 100, 3]
    arr2 = [-5, -2, 10, -3, 7]
    d = 6
    print(findTheDistanceValue(arr1, arr2, d))
