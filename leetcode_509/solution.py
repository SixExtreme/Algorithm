class Solution:
    def fib(self, N: int) -> int:
        fa, fb = 0, 1
        for _ in range(N):
            fa, fb = fb, fa + fb
        return fa


def test_solution():
    assert Solution().fib(0) == 0
    assert Solution().fib(1) == 1
    assert Solution().fib(2) == 1
    assert Solution().fib(3) == 2
    assert Solution().fib(4) == 3
