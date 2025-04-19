# first thougth
def arrayPairsum(nums):
    nums = sorted(nums)
    sum = 0
    for i in range(0,len(nums),2):
        sum += min(nums[i], nums[i+1])
    return sum

# from discussion using list comprehension
def arrayPairsumLC(nums):
    nums = sorted(nums)
    # to select the even indexed values
    min_vlaues = [min(nums[i], nums[i + 1]) for i, x in enumerate(nums) if i % 2 == 0]
    # we can just do
    # nums[0::2] # gives same result
    return sum(min_vlaues)

if __name__ == '__main__':
    nums = [1,4,3,2]
    print(arrayPairsumLC(nums))
