# New solution
from collections import Counter
def intersect(self, nums1, nums2):
    a, b = map(Counter, (nums1, nums2))
    return list((a & b).elements())


def intersect(nums1, nums2):
    count1 = {}
    count2 = {}
    for num in nums1:
        count1[num]= count1.get(num, 0) +1
    for num in nums2:
        count2[num] = count2.get(num, 0) + 1
    intersection_set = set(nums1).intersection(set(nums2))
    output = []
    for x in intersection_set:
        freq = min(count1[x], count2[x])
        output.extend([x]*freq)
    return output
# best method on leetcode
# the method is almost same but it doesn't use the built in methods like extend.
def intersectBest(nums1, nums2):
    dict1 = {}
    dict2 = {}
    result = []
    for num in nums1:
        if num not in dict1:
            dict1[num] = 1
        else:
            dict1[num] += 1
    for num in nums2:
        if num not in dict2:
            dict2[num] = 1
        else:
            dict2[num] += 1

    for k in dict1:
        if k in dict2:
            for i in range(min(dict1[k], dict2[k])):
                result.append(k)

    return result

if __name__ == '__main__':
    # nums1 = [1, 2, 2, 1]
    # nums2 = [2, 2]
    nums1 = [2,1]
    nums2 = [1,1]
    print(intersect(nums1, nums2))