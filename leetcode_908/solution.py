class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        """
        Add x to elems of A, -K <= x <= K
        let lim[max(A) - min(A)] = 0
        """
        _min = _max = A[0]
        for a in A:
            if a > _max:
                _max = a
            if a < _min:
                _min = a
        # everyone can modify to same value
        if _max - K <= _min + K:
            return 0
        return (_max - K) - (_min + K)