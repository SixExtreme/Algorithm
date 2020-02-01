class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # from math import factorial as A
        # return int(A(m + n - 2) / A(m - 1) / A(n - 1))

        dp = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            dp[i][0] = 1
        for j in range(m):
            dp[0][j] = 1
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[n-1][m-1]

        # pre, cur = [1] * n, [1] * n
        # for i in range(1, m):
        #     for j in range(1, n):
        #         cur[j] = pre[j] + cur[j-1]
        #     pre = cur[:]
        # return pre[-1]

        # cur = [1] * n
        # for i in range(1, m):
        #     for j in range(1, n):
        #         cur[j] += cur[j - 1]
        # return cur[-1]


def test_solution():
    print("cases")
    assert Solution().uniquePaths(3, 2) == 3
    # assert Solution().uniquePaths(7, 3) == 28
    # assert Solution().uniquePaths(57, 2) == 57
