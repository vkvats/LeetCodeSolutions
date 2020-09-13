# New method
# using binary search
class Solution:
    def countNegatives(self, grid: [[int]]) -> int:
        count = 0
        if not grid: return count
        for g in grid:
            # binary search in grid
            lo, hi = 0, len(g)
            while lo < hi:
                mid = (lo + hi) // 2
                if g[mid] >= 0:
                    lo = mid + 1
                else:
                    hi = mid
            if lo != len(g):
                count += len(g) - lo
        return count



# using list methods only

class Solution1:
    def countNegatives(self, grid: [[int]]) -> int:
        count = 0
        for row in grid:
            for val in row:
                if val < 0: count += 1
                else: break # this should give advantage in large matrix
        return count

# first thought
def countNegatives(grid):
    import numpy as np
    array = np.array(grid)
    return np.sum(array<0)

# from discussion (faster solution)
def countNegativesLC(self, grid):
    result = [y for x in grid for y in x if y < 0]

    return len(result)
if __name__ == '__main__':
    # grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
    # grid = [[3, 2], [1, 0]]
    grid = [[1, -1], [-1, -1]]
    print(Solution().countNegatives(grid))