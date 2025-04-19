class Solution:

    def orangesRotting(self, grid: [[int]]) -> int:
        minutes = 0
        self.visited = []
        queue = []
        self.r, self.c = len(grid), len(grid[0])
        queue_org = self.get_rotten(grid)
        while queue_org:
            tmp2 = []
            while queue_org:
                ri, rj = queue_org.pop()
                if [ri,rj] not in self.visited:
                    self.visited.append([ri, rj])
                    tmp = self.visit(grid, ri, rj)
                    tmp2.extend(tmp)
            queue_org = [val for val in tmp2 if grid[val[0]][val[1]] == 1]
            minutes += 1

        for row in range(self.r):
            if 1 in grid[row]: return -1
        return minutes

    def visit(self, grid, ri, rj):
        t1 = t2 = t3 = t4 = []
        if rj + 1 < self.c and grid[ri][rj + 1] == 1:
            grid[ri][rj + 1] = 2
            if [ri, rj + 1] not in self.visited:
                t1 = self.rotten_check(grid, ri, rj + 1)
        if rj - 1 >= 0 and grid[ri][rj - 1] == 1:
            grid[ri][rj - 1] = 2
            if [ri, rj - 1] not in self.visited:
                t2 = self.rotten_check(grid, ri, rj - 1)
        if ri + 1 < self.r and grid[ri + 1][rj] == 1:
            grid[ri + 1][rj] = 2
            if [ri + 1, rj] not in self.visited:
                t3 = self.rotten_check(grid, ri + 1, rj)
        if ri - 1 >= 0 and grid[ri - 1][rj] == 1:
            grid[ri - 1][rj] = 2
            if [ri - 1, rj] not in self.visited:
                t4 = self.rotten_check(grid, ri - 1, rj)
        return t1 + t2 + t3 + t4



    def get_rotten(self, grid):
        queue = []
        for i in range(self.r):
            for j in range(self.c):
                if grid[i][j] == 2:
                    if j + 1 < self.c and grid[i][j + 1] == 1:
                        queue.append([i, j])
                    elif j - 1 >= 0 and grid[i][j - 1] == 1:
                        queue.append([i, j])
                    elif i + 1 < self.r and grid[i + 1][j] == 1:
                        queue.append([i, j])
                    elif i - 1 >= 0 and grid[i - 1][j] == 1:
                        queue.append([i, j])
        return queue

    def rotten_check(self, grid, i, j):
        queue = []
        if j + 1 < self.c and grid[i][j + 1] == 1:
            queue.append([i, j])
        elif j - 1 >= 0 and grid[i][j - 1] == 1:
            queue.append([i, j])
        elif i + 1 < self.r and grid[i + 1][j] == 1:
            queue.append([i, j])
        elif i - 1 >= 0 and grid[i - 1][j] == 1:
            queue.append([i, j])
        return queue



if __name__ == '__main__':
    g = [[2,2],[1,1],[0,0],[2,0]] #[[1,1,2,0,2,0, 1]] # [[1,2]] # [[2, 1, 1], [1, 1, 0], [0, 1, 1]]  # [[1],[2],[1],[2]] #
    print(Solution().orangesRotting(g))