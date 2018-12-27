class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        dp1, dp2 = 1, 2
        for i in range(2, n):
            dp1, dp2 = dp2, dp1 + dp2
        return dp2


if __name__ == '__main__':
    print(Solution().climbStairs(4))