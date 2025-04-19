# New solution using Dictionary
from collections import defaultdict
class Solution:
    def minimumAbsDifference(self, arr: [int]) -> [[int]]:
        arr.sort() # O(nlog(n))
        min_diff = float('inf')
        for i in range(1, len(arr)): # order N
            diff = arr[i] - arr[i-1]
            if diff < min_diff: min_diff = diff
        output = defaultdict(list)
        for i in range(1, len(arr)): # order N
            diff = arr[i] - arr[i-1]
            if diff == min_diff:
                output[min_diff].append([arr[i-1], arr[i]])
        return output[min_diff]

# same solution in 3 lines
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mn = min(b - a for a, b in zip(arr, arr[1:]))
        return [[a, b] for a, b in zip(arr, arr[1:]) if b - a == mn]



class Solution:
    def minimumAbsDifference(self, arr: [int]) -> [[int]]:
        arr.sort() # O(nlog(n))
        val = float('inf')
        for i in range(len(arr) - 1): # O(n)
            diff = arr[i+1] - arr[i]
            if diff < val:
                val = diff
        sol = [ [arr[i], arr[i+1]] for i in range(len(arr) - 1) if arr[i+1] - arr[i] == val] # O(n)
        return sol

    # modification
    def minimumAbsDifference2(self, arr: [int]) -> [[int]]:
        arr.sort() # O(nlog(n))
        val = float('inf')
        sol = []
        for i in range(len(arr) - 1): # O(n)
            diff = arr[i+1] - arr[i]
            if diff < val:
                val = diff
                sol = [[arr[i], arr[i+1]] ]
            elif diff == val:
                sol.append([arr[i], arr[i+1]])
        return sol

# total time complexity n log(n) + n + n

# Solutions from leetcode
class SolutionF1:
    def minimumAbsDifference(self, arr):
        arr.sort() # n.log(n)
        cur_min = float('inf')
        ans = []
        for i in range(1, len(arr)): # (N)
            cur = arr[i] - arr[i - 1]
            if cur == cur_min:
                ans.append((arr[i - 1], arr[i]))
            elif cur < cur_min:
                cur_min = cur
                ans = [(arr[i - 1], arr[i])]
        return ans


if __name__ == '__main__':
    arr = [40,11,26,27,-20]
    sol = Solution().minimumAbsDifference(arr)
    print(sol)