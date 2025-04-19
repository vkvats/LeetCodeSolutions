class Solution:
    def searchRange(self, nums: [int], target: int) -> [int]:
        self.finalRange = [-1, -1]
        self.binarySearch(nums, target, 0, len(nums) - 1, True)
        self.binarySearch(nums, target, 0, len(nums) - 1, False)
        return self.finalRange

    def binarySearch(self, nums, target, left, right, goLeft):
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                if goLeft:
                    if mid == 0 or nums[mid - 1] != target:
                        self.finalRange[0] = mid
                        return
                    else:
                        right = mid - 1
                else:
                    if mid == len(nums) - 1 or nums[mid + 1] != target:
                        self.finalRange[1] = mid
                        return
                    else:
                        left = mid + 1

    def binarySearchRecursive(self, nums, target, left, right, goLeft):
        if left > right:
            return
        mid = (left + right) // 2
        if nums[mid] < target:
            self.binarySearchRecursive(nums, target, mid + 1, right, goLeft)
        elif nums[mid] > target:
            self.binarySearchRecursive(nums, target, left, mid - 1, goLeft)
        else:
            if goLeft:
                if mid == 0 or nums[mid - 1] != target:
                    self.finalRange[0] = mid
                    return
                else:
                    self.binarySearchRecursive(nums, target, left, mid - 1, goLeft)
            else:
                if mid == len(nums) - 1 or nums[mid + 1] != target:
                    self.finalRange[1] = mid
                    return
                else:
                    self.binarySearchRecursive(nums, target, mid + 1, right, goLeft)

# Solution from leetcode
class SolutionFast1:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # if there's no nums,
        if not nums:
            return [-1, -1]

        def find_left(nums, target):

            # figure left and right,
            left = 0
            right = len(nums) - 1

            while left < right:

                # find mid,
                mid = left + (right - left) // 2

                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid

            return left if nums[left] == target else - 1

        def find_right(nums, target):

            # figure left and right,
            left = 0
            right = len(nums) - 1

            while left < right:

                # find mid,
                mid = (left + (right - left) // 2) + 1

                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid

            return left if nums[left] == target else - 1

        # find left,
        left = find_left(nums, target)
        right = find_right(nums, target)

        return [left, right]

if __name__ == '__main__':
    arr = [1,3, 3, 3]
    target = 3
    print(Solution().searchRange(arr, target))




