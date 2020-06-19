def rob(nums):
    if (len(nums) == 0): return 0
    if (len(nums) == 1): return nums[0]

    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
    return max(dp[-1], dp[-2])

# fastest solution
def robFast(nums):
    e = i = 0
    for x in nums:
        e, i = i, max(e + x, i)
    return max(e, i)

# second fastest
def rob(nums):
    for i in range(2, len(nums)):
        nums[i] += max(nums[:i - 1])
    return max(nums) if nums else 0

if __name__ == '__main__':
    # nums = [1,2,3,1]
    # nums = [2, 7, 9, 3, 1]
    nums = [2,1,1,2]
    print(rob(nums))