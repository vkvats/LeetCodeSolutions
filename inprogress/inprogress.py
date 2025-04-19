from typing import List, Dict, Tuple


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = None, None
        total_len = len(nums1) + len(nums2)
        merged_list = []
        ## we do not need to iterate over full length of the joint list
        if total_len % 2 ==0: 
            itr_len = total_len//2 + 1
        else: 
            itr_len = (total_len+1)//2
        ## Iterate till mid-point
        for _ in range(itr_len): 
            if n1 is None and len(nums1) != 0: 
                n1 = nums1.pop(0)
            if n2 is None and len(nums2) != 0: 
                n2 = nums2.pop(0)
            ## If one list if empty first
            if n1 is None and n2 is not None: ## means nums1 is empty 
                merged_list.append(n2)
                n2 = None
                # merged_list.extend(nums2)
            if n2 is None and n1 is not None: ## means nums2 is empty
                merged_list.append(n1)
                n1 = None
                # merged_list.extend(nums1)
            ## while both list has elements
            if n1 is not None and n2 is not None: 
                if n1 <= n2: 
                    merged_list.append(n1)
                    n1 = None
                else:
                    merged_list.append(n2) 
                    n2 = None
        ## find median when total_len is odd and even
        # print(f"Merged list:{merged_list}")
        if total_len % 2 == 0: 
            return (merged_list[-2] + merged_list[-1])/2
        else: 
            return merged_list[-1]


s = Solution()
nums1, nums2 = [1,2,], [3,4]
print(s.findMedianSortedArrays(nums1, nums2))