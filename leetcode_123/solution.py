from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        n = len(prices)
        dpl, dpr = [0] * n, [0] * n

        i, j = 1, n - 2
        _min, _max = prices[0], prices[n - 1]
        while i < n and j > -1:
            _min = min(_min, prices[i])
            dpl[i] = max(dpl[i - 1], prices[i] - _min)
            i += 1
            _max = max(_max, prices[j])
            dpr[j] = max(dpr[j + 1], _max - prices[j])
            j -= 1
        profit = 0
        for k in range(1, n - 1):
            profit = max(profit, dpl[k] + dpr[k + 1])
        return max(dpl[n - 1], profit)









if __name__ == '__main__':
    print(Solution().maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
    print(Solution().maxProfit([1, 2, 3, 4, 5]))
    print(Solution().maxProfit([7, 6, 4, 3, 1]))
    print(Solution().maxProfit([7, 11, 4, 1, 2]))
