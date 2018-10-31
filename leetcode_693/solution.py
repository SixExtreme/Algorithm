class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # n =         1 0 1 0 1 0 1 0
        # n >> 1      0 1 0 1 0 1 0 1
        # n ^ n>>1    1 1 1 1 1 1 1 1
        # n           1 1 1 1 1 1 1 1
        # n + 1     1 0 0 0 0 0 0 0 0
        # n & (n+1)   0 0 0 0 0 0 0 0

        n ^= (n >> 1)
        return not n & n + 1
