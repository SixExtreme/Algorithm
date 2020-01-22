from typing import List


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        _mul, _add = 1, 0
        while n:
            t = n % 10
            _mul *= t
            _add += t
            n //= 10
        return _mul - _add


def test_solution():
    assert Solution().subtractProductAndSum(234) == 15
    assert Solution().subtractProductAndSum(4421) == 21
