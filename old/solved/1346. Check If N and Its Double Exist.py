# New method
# using set() for visited
class Solution:
    def checkIfExist(self, arr: [int]) -> bool:
        visited = set()
        for num in arr:
            if 2 * num in visited or num / 2 in visited: return True
            visited.add(num)
        return False

# Using Hashma
from collections import Counter
class Solution:
    def checkIfExist(self, arr: [int]) -> bool:
        freq = Counter(arr)
        for num in arr:
            if freq[2*num] and num != 0: return True
            elif freq[0] >= 2 and num == 0: return True
        return False

class Solution:
    def checkIfExist(self, arr: [int]) -> bool:
        twice_nums = [2*num for num in arr]
        if 0 in arr:
            zero_count = arr.count(0)
            if zero_count >= 2:
                return True
            else:
                arr.remove(0)
        intersection = set(arr).intersection(set(twice_nums))
        print(intersection)
        if intersection:
            return True
        else:
            return False

# Solution from leetcode
class SolutionF1:
    def checkIfExist(self, arr):
        # this will handle the case of two zeros efficiently.
        # as when we are checking in set values, we dont have 0 added to that set.
        values = set()
        for num in arr:
            if 2 * num in values or num / 2 in values:
                return True
            values.add(num)

# Solution from leetcode (linear search)
class SolutionF2:
    def checkIfExist(self, arr: [int]) -> bool:
        if not arr:
            return False
        cnt = 0
        for i in arr:
            if i == 0:
                cnt += 1
            if cnt >= 2:
                return True
            if i != 0 and i * 2 in arr:
                return True
        return False

        return False