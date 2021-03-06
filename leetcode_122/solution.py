class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(1, len(prices)):
            delta = prices[i] - prices[i - 1]
            if delta > 0:
                profit += delta
        return profit

