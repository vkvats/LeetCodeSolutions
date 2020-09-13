class SolutionMethod1:
    def pivotIndex(self, nums: [int]) -> int:
        if len(nums) <=2: return -1
        s = sum(nums)
        left_sum = 0
        for idx, n in enumerate(nums):
            if left_sum == (s - left_sum - n):
                return idx
            left_sum += n
        return -1

# Solution from leetcode (same as above)
class SolutionF1:
    def pivotIndex(self, nums: [int]) -> int:
        left , right = 0, sum(nums)
        for index, num in enumerate(nums):
            right -= num
            if left == right:
                return index
            left += num
        return -1



if __name__ == '__main__':
    nums = [1,7,3,6,5,6]
    nums = [-1,-1,-1,0,1,1]
    print(Solution().pivotIndex(nums))