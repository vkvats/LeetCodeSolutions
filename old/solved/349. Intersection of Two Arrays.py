def intersection(nums1, nums2):
    setA = set(nums1)
    setB = set(nums2)
    # one liner
    # return list(set(nums1).intersection(set(nums2)))
    return list(setA.intersection(setB))

if __name__ == '__main__':
    # nums1 = [1, 2, 2, 1]
    # nums2 = [2, 2]
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(intersection(nums1, nums2))