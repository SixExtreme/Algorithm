class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        _ASC, _DES = True, True
        for i in range(1, n):
            if A[i] == A[i - 1]:
                continue
            elif A[i] < A[i - 1] and _ASC:
                _ASC = False
            elif A[i] > A[i - 1] and _DES:
                _DES = False
        return _ASC or _DES


if __name__ == '__main__':
    A = [1, 3, 2]
    print(Solution().isMonotonic(A))
