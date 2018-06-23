class Solution:
    def peakIndexInMountainArray(self, A: list):
        """
        :type A: List[int]
        :rtype: int
        """
        l, r = 0, len(A) - 1
        while l < r:
            mid = (l + r) // 2
            if A[mid] < A[mid + 1]:
                l = mid
            elif A[mid] < A[mid - 1]:
                r = mid
            else:
                return mid