class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ret = [
            [1 for _ in range(k + 1)]
            for k in range(numRows)
        ]
        for i in range(numRows):
            for j in range(1, i):
                ret[i][j] = ret[i - 1][j - 1] + ret[i - 1][j]
        return ret


if __name__ == '__main__':
    row = 5
    print(Solution().generate(row))
