class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        if m < 3 or n < 3:
            return 0
        count = 0
        for i in range(m - 2):
            for j in range(n - 2):
                valid = True
                # 范围检查
                for di in range(3):
                    for dj in range(3):
                        if grid[i + di][j + dj] < 1:
                            valid = False
                        if grid[i + di][j + dj] > 9:
                            valid = False

                # 斜向
                if valid:
                    if grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2] != 15:
                        valid = False
                    if grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j] != 15:
                        valid = False

                # 横向
                if valid:
                    for di in range(3):
                        if grid[i + di][j] + grid[i + di][j + 1] + grid[i + di][j + 2] != 15:
                            valid = False
                            break
                # 竖向
                if valid:
                    for dj in range(3):
                        if grid[i][j + dj] + grid[i + 1][j + dj] + grid[i + 2][j + dj] != 15:
                            valid = False
                            break
                count += valid
        return count


if __name__ == '__main__':
    grid = [
        [4, 3, 8, 4],
        [9, 5, 1, 9],
        [2, 7, 6, 2]
    ]
    print(Solution().numMagicSquaresInside(grid))
