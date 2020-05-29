def containsDuplicate(nums):
    return not len(set(nums)) == len(nums)

if __name__ == '__main__':
    nums = [1,2,3,1]
    nums = [1,2,3,4]
    nums= [1,1,1,3,3,4,3,2,4,2]
    print(containsDuplicate(nums))