class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        _min, profit = prices[0], 0
        for i in range(1, len(prices)):
            if prices[i] < _min:
                _min = prices[i]
            else:
                delta = prices[i] - _min
                if delta > profit:
                    profit = delta
        return profit