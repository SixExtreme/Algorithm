class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return list(zip(*A))
        # if not A:
        #     return A
        # return [[a[i] for a in A]for i in range(len(A[0]))]