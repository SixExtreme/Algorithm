class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        # _not = lambda x: (x + 1) % 2
        # n = len(A[0])
        # for row in A:
        #     for i in range(n // 2):
        #         row[i], row[-i - 1] = _not(row[-i - 1]), _not(row[i])
        #     if n % 2 != 0:
        #         row[n // 2] = _not(row[n // 2])
        # return A

        return [[1 ^ x for x in row[::-1]] for row in A]

if __name__ == '__main__':
    A = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    ret = Solution().flipAndInvertImage(A)
    print(ret)