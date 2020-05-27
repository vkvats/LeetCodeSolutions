# First thought solution
def createTargetArray(nums, index):
    target = []
    while len(nums)!=0:
        num = nums.pop(0)
        num_index = index.pop(0)
        target.insert(num_index, num)
    return target

# from discussion
def createTargetArrayLC(nums, index):
    target = []
    for i in range(len(nums)): target.insert(index[i], nums[i])
    return target

if __name__ == '__main__':
    nums = [0, 1, 2, 3, 4]
    index = [0, 1, 2, 2, 1]
    # nums = [1, 2, 3, 4, 0]
    # index = [0, 1, 2, 3, 0]
    # nums = [1]
    # index = [0]
    print(createTargetArrayLC(nums, index))