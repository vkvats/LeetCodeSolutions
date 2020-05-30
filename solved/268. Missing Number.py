def missingNumber(nums):
    nums_set = set(nums)
    actual_set = set(range(len(nums)+1))
    return list(actual_set - nums_set)[0]
# best solutionm
def missingNumberBest(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)

if __name__ == '__main__':
    nums = [3,0,1]
    # nums = [9,6,4,2,3,5,7,0,1]
    nums =[0]
    print(missingNumber(nums))