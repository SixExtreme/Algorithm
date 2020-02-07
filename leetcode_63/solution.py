from typing import List


class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        if grid[0][0] == 1:
            return 0
        grid[0][0] = 1
        m, n = len(grid), len(grid[0])
        for i in range(1, n):
            if grid[0][i] == 1:
                grid[0][i] = 0
            else:
                grid[0][i] = grid[0][i - 1]
        for j in range(1, m):
            if grid[j][0] == 1:
                grid[j][0] = 0
            else:
                grid[j][0] = grid[j - 1][0]
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                else:
                    grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        return grid[m - 1][n - 1]


def test_solution():
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    assert Solution().uniquePathsWithObstacles(grid) == 2
