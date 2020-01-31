class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        if X >= Y:
            return X - Y
        ans = 0
        while Y > X:
            ans += 1
            if Y % 2 == 1:
                Y += 1
            else:
                Y //= 2
        return ans + (X - Y)


def test_solution():
    assert Solution().brokenCalc(2, 3) == 2
    assert Solution().brokenCalc(5, 8) == 2
    assert Solution().brokenCalc(3, 10) == 3
    assert Solution().brokenCalc(1024, 1) == 1023
