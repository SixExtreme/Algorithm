class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(M), len(M[0])
        ret = [[0 for _ in range(n)] for _ in range(m)]
        directs = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                   (0, 1), (1, -1), (1, 0), (1, 1)]

        for i in range(m):
            for j in range(n):
                _cnt, _sum = 1, M[i][j]
                for direct in directs:
                    di, dj = direct
                    if 0 <= i + di < m and 0 <= j + dj < n:
                        _cnt, _sum = _cnt + 1, _sum + M[i + di][j + dj]
                ret[i][j] = int(_sum / _cnt)

        return ret


if __name__ == '__main__':
    M = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    print(Solution().imageSmoother(M))