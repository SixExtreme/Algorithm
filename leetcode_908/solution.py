class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        B = []
        _min, _max = 0, 0
        for x in A:
            if x > K:
                t = K
            elif x < -K:
                t = -K
            else:
                if K + x < K - x:
                    B.append(-K)
                else:
                    B.append(K)


        return B

if __name__ == '__main__':
    A, K = [1, 3, 6], 3
    print(Solution().smallestRangeI(A, K))