class SolutionLinearSearch:
    def findPeakElement(self, nums: [int]) -> int:
        # Linear search # stop where you find the first peak
        # but this method will always give the first peak
        # O(n)
        for i in range(1, len(nums) - 1):
            if (nums[i - 1] < nums[i]) and (nums[i] > nums[i + 1]):
                return i
        # we have not checked the first and the last elements
        if nums[0] > nums[-1]:
            return 0
        else:
            return len(nums) - 1

class SolutionBS: # template III
    def findPeakElement(self, nums: [int]) -> int:
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



if __name__ == '__main__':
    nums = [1,2,1,3,5,6,4]
    print(SolutionBS().findPeakElement(nums))
