def twoSum(numbers, target):
    # the numbers array is sorted, so we shoule unitlize that for faster search.
    # technically, it can be done in a single round.
    i = 0 # start from start
    j = len(numbers) - 1 # start from end.

    while i < j and numbers[i] + numbers[j] != target: # if the number are not same then
        # decrease the J by 1 because we need to add smaller number.
        if numbers[i] + numbers[j] > target:
            j = j - 1
        else:
            # we increase the i by 1 because we need to add larger number.
            i = i + 1

    return [i + 1, j + 1]


# fastest solution
def twoSumFast(numbers, target):
    res = {}
    for index, value in enumerate(numbers):
        rest = target - value
        if rest in res:
            return [res[rest], index + 1]
        else:
            res[value] = index + 1



if __name__ == '__main__':
    numbers = [0,0,3,4] # [5,25,75] #[2,7,11,15]
    target = 0
    print(twoSumFast(numbers, target))