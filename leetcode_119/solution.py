class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ret = [1 for _ in range(rowIndex + 1)]
        for i in range(2, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                ret[j] += ret[j - 1]
        return ret


if __name__ == '__main__':
    print(Solution().getRow(5))