class Solution:
    def threeSumClosest(self, nums: [int], target: int) -> int:
        nums.sort()
        sums = float('inf')
        for i in range(len(nums) - 2):
            s = sum(nums[i: i + 3])
            if sums > abs(s - target):
                sums = abs(s - target)
        return sums + target

if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    target = 1
    print(Solution().threeSumClosest(nums, target))