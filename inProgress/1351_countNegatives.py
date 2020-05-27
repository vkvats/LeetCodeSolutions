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
    print(countNegatives(grid))