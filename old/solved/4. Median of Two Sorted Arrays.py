class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        new_arr = nums1 + nums2
        new_arr.sort()
        n = len(new_arr)
        if n % 2 == 0:
            return (new_arr[n // 2 - 1] + new_arr[n // 2]) / 2
        else:
            return new_arr[n // 2]

# other implementation could be
# writing sorting algo, if built in sorting is not allowed to be used
# merging two arrays to make a sorted array

class SolutionM2:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        new_arr = self.merge(nums1, nums2)
        print(new_arr)
        n = len(new_arr)
        if n % 2 == 0:
            return (new_arr[n // 2 - 1] + new_arr[n // 2]) / 2
        else:
            return new_arr[n // 2]

    def merge(self, a1, a2):
        arr = []
        i1, i2 = 0, 0
        while i1 < len(a1) and i2 < len(a2):
            val1 = a1[i1]
            val2 = a2[i2]
            if val1 <= val2:
                arr.append(val1)
                i1 += 1
            elif val2 < val1:
                arr.append(val2)
                i2 += 1
        if i2 == len(a2) and i1 < len(a1):
            arr.extend(a1[i1:])
        elif i1 == len(a1) and i2 < len(a2):
            arr.extend(a2[i2:])
        return arr

a1 = [1,2]
a2 = [3,4]
print(merge(a1, a2))