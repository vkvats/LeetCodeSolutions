class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        product1 = nums[-3] * nums[-2] * nums[-1]
        product2 = nums[0] * nums[1] * nums[-1]
        return (max(product1, product2))

# Solution from leetcode

class SolutionF1:
    def maximumProduct(self, nums: List[int]) -> int:
        # trick, 3 variables for maximums, 2 min variables for negative values
        # find the max among product of 3 max and product of 2 min and max3

        max1, max2, max3 = float('-inf'), float('-inf'), float('-inf')
        min1, min2 = float('inf'), float('inf')
        negativeCtr = 0

        # first look for 3 max
        for n in nums:
            if n > max3:
                max3, max2, max1 = n, max3, max2
            elif n > max2:
                max2, max1 = n, max2
            elif n > max1:
                max1 = n

            if n < min2:
                min2, min1 = n, min2
            elif n < min1:
                min1 = n

        return max(max3 * max2 * max1, min1 * min2 * max3)

# Solution from leetcode
