class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        dp0, dp1 = 1, 2
        for i in range(2, n):
            dp0, dp1 = dp1, dp0 + dp1
        return dp1


if __name__ == '__main__':
    print(Solution().climbStairs(4))