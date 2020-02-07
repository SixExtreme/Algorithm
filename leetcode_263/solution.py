class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        if num == 1:
            return True
        tmp = num
        while tmp != 1:
            last = tmp
            if tmp % 2 == 0:
                tmp //= 2
            if tmp % 3 == 0:
                tmp //= 3
            if tmp % 5 == 0:
                tmp //= 5
            if tmp == last:
                break
        return tmp == 1


def test_solution():
    assert Solution().isUgly(6)
    assert Solution().isUgly(8)
    assert not Solution().isUgly(14)
