def shiftGrid(grid, k):
    col_num = len(grid[0])
    row_num = len(grid)
    for _ in range(k):
        newgrid = [[None for _ in range(row_num)] for _ in range(col_num)]
        newgrid[0][0] = grid[row_num - 1][col_num - 1]
        for i in range(row_num):
            for j in range(1, col_num):
                if j <= col_num-1:
                    newgrid[i][j] = grid[i][j-1]
                    if newgrid[i][col_num-1] and not newgrid[row_num - 1][col_num - 1]:
                        i +=1
                        newgrid[i][0] = grid[i - 1][j]
                    if newgrid[row_num - 1][col_num - 1]:
                        break
        grid = newgrid
    if col_num == 1 and row_num == 1:
        return grid
    else:
        return newgrid


if __name__ == '__main__':
    # grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # k = 9
    # grid = [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]]
    # k = 4
    grid = [[1],[2],[3],[4],[7],[6],[5]]
    k = 23

    print(shiftGrid(grid, k))