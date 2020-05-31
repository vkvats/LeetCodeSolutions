def findErrorNums(nums):
    n = len(nums)
    original_set = set(range(1, n+1))
    missing_num = list(original_set - set(nums))[0]
    diff = int(n*(n+1)/2 - sum(nums))
    return [missing_num-diff, missing_num]

# best solution on leetcode
def findErrorNums(nums):
    # alpha = twice - never
    # beta = twice + never
    # sum(A) - never + twice = sum(1...N) => alpha = sum(A) - N*(N+1) / 2
    N = len(nums)
    alpha = sum(nums) - N * (N + 1) / 2

    # sum(x*x for x in A) - twice*twice + never*never = sum(1*1...N*N)
    beta = (sum(x * x for x in nums) - N * (N + 1) * (2 * N + 1) / 6) / alpha

    return int((alpha + beta) / 2), int((beta - alpha) / 2)


if __name__ == '__main__':
    nums = [1, 2, 2, 4]
    print(findErrorNums(nums))