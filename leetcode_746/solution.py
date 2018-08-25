class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        dp0, dp1 = 0, 0
        for i in range(2, n + 1):
            step2 = dp0 + cost[i - 2]
            step1 = dp1 + cost[i - 1]
            dp0, dp1 = dp1, min(step2, step1)
        return dp1


if __name__ == '__main__':
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(Solution().minCostClimbingStairs(cost))
