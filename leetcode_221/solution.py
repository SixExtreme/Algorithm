from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # if len(matrix) == 0 or len(matrix[0]) == 0:
        #     return 0
        # ans = 0
        # m, n = len(matrix), len(matrix[0])
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] != '1':
        #             continue
        #         k, flag = 1, True
        #         while flag and i + k < m and j + k < n:
        #             for _i in range(i, i + k + 1):
        #                 if matrix[_i][j] == '0':
        #                     flag = False
        #                     break
        #             for _j in range(j, j + k + 1):
        #                 if matrix[i][_j] == '0':
        #                     flag = False
        #                     break
        #             if flag:
        #                 k += 1
        #         ans = max(ans, k * k)
        # return ans

        # if len(matrix) == 0 or len(matrix[0]) == 0:
        #     return 0
        # k = 0
        # m, n = len(matrix), len(matrix[0])
        # dp = [[0] * (n + 1) for _ in range(m + 1)]
        # for i in range(1, m + 1):
        #     for j in range(1, n + 1):
        #         if matrix[i - 1][j - 1] == '0':
        #             continue
        #         dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        #         k = max(k, dp[i][j])
        # return k * k

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        k, prev = 0, 0
        m, n = len(matrix), len(matrix[0])
        dp = [0 for _ in range(n + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                tmp = dp[j]
                if matrix[i - 1][j - 1] == '0':
                    dp[j] = 0
                else:
                    dp[j] = min(prev, dp[j], dp[j - 1]) + 1
                    k = max(k, dp[j])
                prev = tmp
        return k * k


def test_solution():
    matrix = [
        ['0', '0', '0', '1'],
        ['1', '1', '0', '1'],
        ['1', '1', '1', '1'],
        ['0', '1', '1', '1'],
        ['0', '1', '1', '1']
    ]
    assert Solution().maximalSquare(matrix) == 9

    matrix = [
        ['1', '0', '1', '0', '0'],
        ['1', '0', '1', '1', '1'],
        ['1', '1', '1', '1', '1'],
        ['1', '0', '0', '1', '0']
    ]
    assert Solution().maximalSquare(matrix) == 4

    matrix = [
        ['1', '1'],
        ['1', '1']
    ]
    assert Solution().maximalSquare(matrix) == 4
