from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # n = len(triangle)
        # if n == 0:
        #     return 0
        #
        # dp = [[0] * i for i in range(1, n + 1)]
        # dp[0][0] = triangle[0][0]
        #
        # for i in range(1, n):
        #     for j in range(i + 1):
        #         if j == 0:
        #             dp[i][j] = dp[i - 1][j] + triangle[i][j]
        #         elif j == i:
        #             dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
        #         else:
        #             dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
        # return min(dp[n - 1])

        # n = len(triangle)
        # if n == 0:
        #     return 0
        #
        # dp = [x for x in triangle[n - 1]]
        # for i in range(n - 2, -1, -1):
        #     for j in range(i + 1):
        #         dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        # return dp[0]

        n = len(triangle)
        if n == 0:
            return 0

        dp = [0] * n
        for i in range(n - 1, -1, -1):
            for j in range(i + 1):
                dp_next = dp[j + 1] if j + 1 < n else 0
                dp[j] = min(dp[j], dp_next) + triangle[i][j]
        return dp[0]


def test_solution():
    triangle = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    assert Solution().minimumTotal(triangle) == 11


