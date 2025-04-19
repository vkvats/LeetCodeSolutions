# my solution using set difference
def findDisappearedNumbers(nums):
    allNums = set(range(1, len(nums)+1))
    present_nums = set(nums)
    return list(allNums - present_nums)

## best solution on leetcode
def findDisappearedNumbers(nums):
    s = set(nums)
    return [i for i in range(1, len(nums) + 1) if i not in s]

if __name__ == '__main__':
    nums = [4,3,2,7,8,2,3,1]
    nums = [1,1,1,1,1,1]
    print(findDisappearedNumbers(nums))
