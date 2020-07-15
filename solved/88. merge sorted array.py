def merge_return(nums1, m, nums2, n):
    # this methods returns output, but we need to implement it inplace.
    output = []
    i = j = 0
    while i < m and j < n:
        num_i = nums1[i]
        num_j  = nums2[j]
        if num_i <= num_j:
            output.append(num_i)
            i += 1
        else:
            output.append(num_j)
            j += 1
        if i == m:
            output.extend(nums2[j:])
        elif j == n:
            output.extend(nums1[i:])
    return output


def merge(nums1, m, nums2, n):
    # Nodification inplace
    # slick method
    for i in range(m, n+m):
        nums1[i] = nums2[i-m]
    nums1.sort()
    return nums1


def mergeD(nums1, m, nums2, n):
# solution from discussion
    # starting by inserting nums2 into nums1 by comparing from the back
    # i is the last real element from nums1 and k is the inserting position
    i, k = m - 1, m + n - 1

    while nums2 and i >= 0:
        if nums1[i] < nums2[-1]:
            nums1[k] = nums2.pop()
        else:
            nums1[k] = nums1[i]
            i -= 1
        k -= 1

    # if there are still items in nums2, it means we have exhaused nums1
    # which means all the elements in nums2 now are smaller than nums1
    # we simply put the rest of nums2 to the front of nums1
    if nums2:
        nums1[:len(nums2)] = nums2

if __name__ == '__main__':
    nums1, m, nums2, n = [4,0,0,0,0,0], 1,[1,2,3,5,6],5 # [2, 0], 1, [1], 1# [1,2,3,0,0,0], 3, [2,5,6], 3 #
    print(merge(nums1, m, nums2, n))