class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i, j, n = 0, 1, len(A)
        while i < n and j < n:
            if A[i] % 2 != 0 and A[j] % 2 == 0:
                A[i], A[j] = A[j], A[i]
            if A[i] % 2 == 0:
                i += 2
            if A[j] % 2 != 0:
                j += 2
        return A


if __name__ == '__main__':
    A = [4, 2, 5, 7]
    print(Solution().sortArrayByParityII(A))