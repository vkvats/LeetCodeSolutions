class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
            # Slow runner- Fast runner two pointer
            i= j = 0
            while j < len(nums):
                if nums[j] != val:
                    nums[i] = nums[j]
                    i += 1
                    j += 1
                else:
                    j += 1

    def second_method(self, nums, val):
        """When we encounter nums[i] = val we can swap the current element
         out with the last element and dispose the last one. This essentially
         reduces the array's size by 1."""
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i], nums[n - 1] = nums[n - 1], nums[i]
                n -= 1
            else:
                i += 1
        return n

# solution form leetcode
# faster form of two pointer method

class SolutionF1:
    def removeElement(self, nums: [int], val: int) -> int:
        store = 0
        for num in nums:
            if num != val:
                nums[store] = num
                store += 1
        return store

# Solution from leetcode (two pointer reversed)
class SolutionF2:
    def removeElement(self, nums, val):

        i, j = 0, len(nums) -1
        while i <= j:
            while i <= j and nums[i] != val:
                i += 1
            while i <= j and nums[j] == val:
                j -= 1
            if i <= j:
                nums[i] = nums[j]
                i += 1
                j -= 1
        return i

# Solutions from leetcode
class SolutionF4:
    def removeElement(self, nums: [int], val: int) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        del nums[j:]
        return len(nums)

if __name__ == '__main__':
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    print(Solution().removeElement(nums, val))