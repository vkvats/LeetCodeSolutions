class Solution:
    def search(self, nums: [int], target: int) -> bool:
        nums = list(set(nums)) # without changing into set, we can't find answers in array like [2,2,2,2,0,2,2] with target 0
        if len(nums) <= 2: return target in nums
        n = len(nums)
        lo, hi = 0, n - 1
        while lo < hi:
            mid = (lo + hi)//2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else: hi = mid

        # now min val at lo
        rot = lo
        lo = 0
        hi = n - 1
        while lo <= hi:
            mid = (lo + hi)//2
            realmid = (mid + rot) % n
            if nums[realmid] == target: return True
            if nums[realmid] < target:
                lo = mid + 1
            else: hi = mid - 1
        return False

# solution from leetcode
class SolutionF1:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        left = 0
        right = n-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target:
                return True
            if nums[mid] == nums[left] and nums[mid] == nums[right]:
                left+=1
                right-=1
                continue
            if nums[mid] >=nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if nums[mid] < target <=nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        return False

# Solution from leetcode
class SolutionF3:
    def search(self, nums: List[int], target: int) -> bool:
        # o(logn) again
        # 4 cases actually due to duplicate
        # 1) if nums[mid] == target, return True
        # 2) if mid > right, left is sorted
        # left <= target <= mid
        # 3)  right side is sorted
        # mid <= target <= right
        # if nums[mid] == nums[right]
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return True
            elif nums[mid] > nums[right]:  # left sorted
                if nums[left] <= target and target <= nums[mid]:  # answer on left
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] == nums[right]:
                right -= 1  # redo to find new mid
            else:
                if nums[mid] <= target and target <= nums[right]:  # answer on right
                    left = mid + 1
                else:
                    right = mid - 1
        return False


if __name__ == '__main__':
    nums = [2,2,2,0,2,2]
    target = 0
    print(Solution().search(nums, target))