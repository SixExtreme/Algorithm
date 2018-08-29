from queue import deque

class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        _max_area = 0
        m, n = len(grid), len(grid[0])
        flag = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in  range(n):
                if grid[i][j] == 1 and flag[i][j] != 1:
                    flag[i][j] = 1
                    area, queue = 0, deque([(i, j)])
                    while queue:
                        area += 1
                        p, q = queue.popleft()
                        if (0 <= p - 1 < m and 0 <= q < n) and grid[p - 1][q] == 1 and flag[p - 1][q] != 1:
                            queue.append((p - 1, q))
                            flag[p - 1][q] = 1
                        if (0 <= p + 1 < m and 0 <= q < n) and grid[p + 1][q] == 1 and flag[p + 1][q] != 1:
                            queue.append((p + 1, q))
                            flag[p + 1][q] = 1
                        if (0 <= p < m and 0 <= q - 1 < n) and grid[p][q - 1] == 1 and flag[p][q - 1] != 1:
                            queue.append((p, q - 1))
                            flag[p][q - 1] = 1
                        if (0 <= p < m and 0 <= q + 1 < n) and grid[p][q + 1] == 1 and flag[p][q + 1] != 1:
                            queue.append((p, q + 1))
                            flag[p][q + 1] = 1
                    _max_area = max(_max_area, area)

        return _max_area



        # if not grid:
        #     return 0
        # m, n = len(grid), len(grid[0])
        # flag = [[0 for _ in range(n)] for _ in range(m)]
        #
        # def dfs(i, j):
        #     nonlocal flag
        #     ans, flag[i][j] = 1, 1
        #     if (0 <= i - 1 < m and 0 <= j < n) and grid[i - 1][j] == 1 and flag[i - 1][j] != 1:
        #         ans += dfs(i - 1, j)
        #     if (0 <= i + 1 < m and 0 <= j < n) and grid[i + 1][j] == 1 and flag[i + 1][j] != 1:
        #         ans += dfs(i + 1, j)
        #     if (0 <= i < m and 0 <= j - 1 < n) and grid[i][j - 1] == 1 and flag[i][j - 1] != 1:
        #         ans += dfs(i, j - 1)
        #     if (0 <= i < m and 0 <= j + 1 < n) and grid[i][j + 1] == 1 and flag[i][j + 1] != 1:
        #         ans += dfs(i, j + 1)
        #     return ans
        #
        # _max_area = 0
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == 1 and flag[i][j] != 1:
        #             area = dfs(i, j)
        #             _max_area = max(_max_area, area)
        #
        # return _max_area

if __name__ == '__main__':
    grid = [
        [1,1,0,0,0],
        [1,1,0,0,0],
        [0,0,0,1,1],
        [0,0,0,1,1]
    ]
    print(Solution().maxAreaOfIsland(grid))