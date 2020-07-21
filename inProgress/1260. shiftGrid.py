def shiftGrid(grid, k):
    rows = len(grid)
    cols = len(grid[0])
    k = k % (rows* cols) # using cyclic property of grid

    grid_arr = []
    for r in grid:
        grid_arr.extend(r)

    for i in range(k):
        last_val = grid_arr.pop()
        grid_arr.insert(0, last_val)
    # reshape into grid arr original shape
    output = []
    for row_num in range(rows):
        output.append(grid_arr[row_num*cols : row_num*cols + cols])
    return output

# Solution from leetcode
class Solution:
    def shiftGrid(self, grid: [[int]], k: int) -> [[int]]:
        m = len(grid)
        n = len(grid[0])
        k = k % (m * n)

        temp = []
        for row in grid:
            temp.extend(row)

        temp = temp[-k:] + temp[:-k]

        return [temp[r * n:(r * n) + n] for r in range(m)]


if __name__ == '__main__':
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 3
    # grid = [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]]
    # k = 4
    # grid = [[1],[2],[3],[4],[7],[6],[5]]
    # k = 23

    print(shiftGrid(grid, k))