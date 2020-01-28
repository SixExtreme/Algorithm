import math

class Solution:
    def arrangeCoins(self, n: int) -> int:
        # i = 1
        # while n:
        #     if n < i:
        #         break
        #     else:
        #         n -= i
        #         i += 1
        # return i - 1
        return int(math.sqrt(2) * math.sqrt(n + 0.125) - 0.5)


def test_solution():
    assert Solution().arrangeCoins(1) == 1
    assert Solution().arrangeCoins(5) == 2
    assert Solution().arrangeCoins(8) == 3
