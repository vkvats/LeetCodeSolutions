class Solution:
    def findKthLargest(self, nums: [int], k: int) -> int:
        nums.sort()
        return nums[-k]
