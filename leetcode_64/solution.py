from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # m, n = len(grid), len(grid[0])
        # dp = [[0 for _ in range(n)] for _ in range(m)]
        # for i in reversed(range(m)):
        #     for j in reversed(range(n)):
        #         if i == m - 1 and j == n - 1:
        #             dp[i][j] = grid[i][j]
        #         if i == m - 1 and j != n - 1:
        #             dp[i][j] = grid[i][j] + dp[i][j + 1]
        #         if i != m - 1 and j == n - 1:
        #             dp[i][j] = grid[i][j] + dp[i + 1][j]
        #         if i != m - 1 and j != n - 1:
        #             dp[i][j] = grid[i][j] + min(dp[i + 1][j], dp[i][j + 1])
        # return dp[0][0]

        # m, n = len(grid), len(grid[0])
        # dp = [0 for _ in range(n)]
        # for i in reversed(range(m)):
        #     for j in reversed(range(n)):
        #         if i == m - 1 and j == n - 1:
        #             dp[j] = grid[i][j]
        #         if i == m - 1 and j != n - 1:
        #             dp[j] = grid[i][j] + dp[j + 1]
        #         if i != m - 1 and j == n - 1:
        #             dp[j] = grid[i][j] + dp[j]
        #         if i != m - 1 and j != n - 1:
        #             dp[j] = grid[i][j] + min(dp[j], dp[j + 1])
        # return dp[0]

        m, n = len(grid), len(grid[0])
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if i == m - 1 and j == n - 1:
                    continue
                if i == m - 1 and j != n - 1:
                    grid[i][j] += grid[i][j + 1]
                if i != m - 1 and j == n - 1:
                    grid[i][j] += grid[i + 1][j]
                if i != m - 1 and j != n - 1:
                    grid[i][j] += min(grid[i + 1][j], grid[i][j + 1])
        return grid[0][0]


def test_solution():
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    assert Solution().minPathSum(grid) == 7
