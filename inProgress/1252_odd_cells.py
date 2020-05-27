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
    # indices = [[0, 1], [1, 1]]
    n = 2
    m = 2
    indices = [[1, 1], [0, 0]]
    print(oddCells(n,m, indices))
