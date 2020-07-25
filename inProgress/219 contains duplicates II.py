from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: [int], k: int) -> bool:
        num_index = defaultdict(list)
        for idx, num in enumerate(nums):
            num_index[num].append(idx)
        for n in set(nums):
            indicies = num_index[n]
            if len(indicies)>=2:
                for i in range(len(indicies)):
                    id1 = indicies[i]
                    for id2 in indicies[i+1:]:
                        if abs(id1 - id2) <= k:
                            return True
        return False

# we dont even need to get all the indicies before hand
class SolutionF1:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        positions = {}
        for idx, num in enumerate(nums):
            if num in positions and (idx - positions[num] <= k):
                return True
            positions[num] = idx
        return False

##
if __name__ == '__main__':
    nums = [1,2,3,1,2,3] # [1,0,1,1] # [1, 2, 3, 1]
    k = 2 #1 #3
    print(Solution().containsNearbyDuplicate(nums, k))