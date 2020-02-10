from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # if amount == 0:
        #     return 0
        # ans = amount + 1
        # for coin in coins:
        #     if amount - coin < 0:
        #         continue
        #     sub = self.coinChange(coins, amount - coin)
        #     if sub == -1:
        #         continue
        #     ans = min(ans, sub + 1)
        # return ans if ans != amount + 1 else -1

        # def helper(_amt: int, _mem: List[int]):
        #     if _amt == 0:
        #         return 0
        #     if _mem[_amt] != -2:
        #         return _mem[_amt]
        #     res: int = _amt + 1
        #     for coin in coins:
        #         if _amt - coin < 0:
        #             continue
        #         sub = helper(_amt - coin, _mem)
        #         if sub == -1:
        #             continue
        #         res = min(res, sub + 1)
        #     _mem[_amt] = res if res != _amt + 1 else -1
        #     return _mem[_amt]
        #
        # memory = [-2 for _ in range(amount + 1)]
        # return helper(amount, memory)

        dp = [amount + 1 for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                    # print(f'f({i}) = f({i - coin}) + 1', '\t', dp)
        return -1 if dp[amount] > amount else dp[amount]


def test_solution():
    assert Solution().coinChange([1, 2, 5], 11) == 3
    assert Solution().coinChange([2], 3) == -1
    assert Solution().coinChange([2, 5, 10, 1], 27) == 4
