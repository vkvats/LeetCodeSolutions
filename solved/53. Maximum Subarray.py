def maxSubArray(nums):
    """
    exceeds time limit O(n^2)
    """
    # get the maximum value for single number
    max_sum = max(nums)
    # iteration for each size of sub-array and if their sum
    # is greate than max_sum then assign that value to max_sum

    j0 = 2
    while j0 <= len(nums):
        i = 0
        j = j0
        while j <= len(nums):
            new_sum = sum(nums[i:j])
            if new_sum > max_sum:
                max_sum = new_sum
            i += 1
            j += 1
        j0 += 1
    return max_sum

def maxSubArrayDiscussion(nums):
    maxsum = max(sum(nums), *nums)
    sums = 0

    for num in nums:
        sums += num
        if maxsum < sums:
            maxsum = sums
        else:
            if sums < 0:
                sums = 0
    return maxsum

# best solution from leetcode
def maxSubArrayFast(nums):
    max_so_far = nums[0]
    max_ending_here = nums[0]

    for i in range(1, len(nums)):
        max_ending_here = max(max_ending_here + nums[i], nums[i])
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

# 2nd fast solution
def maxSubArray2fast(nums):
    maxNum = nums[0]
    acc = nums[0]
    for n in nums[1:]:
        acc += n
        maxNum = max(acc, maxNum, n)
        if n > acc:
            acc = n
    return maxNum

if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray(nums))