# new solution
class Solution:
    def oddCells(self, n: int, m: int, indices: [[int]]) -> int:
        output = [[0]*m for _ in range(n) ]
        for r,c in indices:
            output[r][:] = [x+1 for x in output[r][:]]
            # we can't access columns of list of list directly by slicing.
            output[:][c] = [x+1 for x in output[:][c]]
        return output


# first thought
def oddCells(n, m, indices):
    import numpy as np
    matrix = np.zeros((n, m))
    for row, col in indices:
        matrix[row, :] += 1
        matrix[:, col] += 1
    return np.sum(matrix % 2 !=0)

if __name__ == '__main__':
    # n = 2
    # m = 3
    indices = [[0, 1], [1, 1]]
    n = 2
    m = 3
    # indices = [[1, 1], [0, 0]]
    print(Solution().oddCells(n, m, indices))
