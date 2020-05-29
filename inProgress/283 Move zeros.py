def moveZeroes(nums):
    # nums2 = nums[:]
    for index, num in enumerate(nums):
        if num ==0:
            nums.remove(0)
            nums.append(0)
    return nums

# alternate method using extend, first we count the total numbers of zeros needed and then add at once
"""This solution isn't fast but gives the solution, also this is not done inplace as asked in the quesiton"""
def moveZeroesExtend(nums):
    count = nums.count(0)
    output = [num for num in nums if num != 0]
    output.extend([0] * count)
    return output

if __name__  == '__main__':
    # nums = [0,1,0,3,12]
    nums = [0,0,1]
    print(moveZeroesExtend(nums))