class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        # i, j = 0, len(A) - 1
        # while i < j:
        #     if A[i] % 2 == 0:
        #         i += 1
        #     elif A[j] % 2 != 0:
        #         j -= 1
        #     elif A[i] % 2 != 0 and A[j] % 2 == 0:
        #         A[i], A[j] = A[j], A[i]
        # return A

        i, j, n = 0, 0, len(A)
        for j in range(n):
            if A[j] % 2 == 0:
                A[i], A[j] = A[j], A[i]
                i += 1
        return A


if __name__ == '__main__':
    A = [0, 1]
    print(Solution().sortArrayByParity(A))


