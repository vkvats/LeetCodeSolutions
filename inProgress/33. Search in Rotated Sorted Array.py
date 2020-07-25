
class Solution:
    def search(self, nums: [int], target: int) -> int:
        # first we need to locate the pivot point
        # to do that we can use finding peak element concept using binary search
        # binary search Template III implementation can help in finding peak element
        # find pivot element
        if not nums: return -1
        if len(nums) <= 2:
            if len(nums) == 2:
                if nums[0] == target:
                    return 0
                elif nums[1] == target:
                    return 1
                else:
                    return -1
            else:
                return 0 if nums[0] == target else -1
        # pivot_index = self.peak_element(nums)
        pivot_index = nums.index(max(nums))
        # now we divie nums in two parts right half, left half and then do the search
        # left half search
        left = self.BS_template_1(nums[:pivot_index + 1], target)
        if left != -1: return left
        if pivot_index != len(nums) - 1:
            right = self.BS_template_1(nums[pivot_index + 1:], target)
            return right + pivot_index + 1 if right != -1 else -1
        else: return left


    def BS_template_1(self, arr, target):
        lo, hi = 0, len(arr) - 1
        while lo <= hi:
            mid = (lo + hi)//2
            if arr[mid] == target:
                return mid
            if arr[mid] < target:
                lo = mid + 1
            else: hi = mid - 1
        return lo if arr[mid] == target else -1

    # not used, failed in one case
    def peak_element(self, nums):
        if len(nums) <= 2:
            if len(nums) == 2:
                return 1 if nums[1] > nums[0] else 0
            else: return 0
        lo, hi = 0, len(nums) - 1
        while lo + 1 < hi:
            mid = (lo + hi)//2
            left = nums[mid - 1]
            right = nums[mid + 1]
            cur = nums[mid]
            if (left < cur) and (right < cur):
                return mid
            elif (left < cur) and (cur < right):
                lo = mid
            else:
                hi = mid
        return 0 if nums[0] > nums[-1] else len(nums) -1

# Solution from leetcode
class SolutionF:
    def search(self, nums: [int], target: int) -> int:

        n = len(nums)
        lo = 0
        hi = n - 1 # only this part is modified from bisect_right code,
        # this modification gives correct index of max value.
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid

        rot = lo
        lo = 0
        hi = n - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            realmid = (mid + rot) % n
            if nums[realmid] == target:
                return realmid
            if nums[realmid] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1


if __name__ == '__main__':
    nums = [57,58,59,62,63,66,68,72,73,74,75,76,77,78,80,81,86,95,96,97,98,100,101,102,103,110,119,120,121,123,125,126,
            127,132,136,144,145,148,149,151,152,160,161,163,166,168,169,170,173,174,175,178,182,188,189,192,193,196,198,
            199,200,201,202,212,218,219,220,224,225,229,231,232,234,237,238,242,248,249,250,252,253,254,255,257,260,266,
            268,270,273,276,280,281,283,288,290,291,292,294,295,298,299,4,10,13,15,16,17,18,20,22,25,26,27,30,31,34,38,
            39,40,47,53,54]
    target = 30
    print(Solution().search(nums, target))