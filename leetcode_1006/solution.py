from typing import List, Optional


class Solution:
    @staticmethod
    def clumsy(n: int) -> int:
        ans: Optional[int] = None
        win: List[int] = []
        while n:
            for _ in range(3):
                win.append(n)
                n -= 1
                if not n:
                    break
            tmp = win[0]
            if len(win) > 1:
                tmp *= win[1]
            if len(win) > 2:
                tmp //= win[2]
            if ans is None:
                ans = tmp
            else:
                ans -= tmp
            if n:
                ans += n
                n -= 1
            win.clear()
        return ans


def test_solution():
    assert Solution.clumsy(1) == 1
    assert Solution.clumsy(2) == 2
    assert Solution.clumsy(3) == 6
    assert Solution.clumsy(4) == 7
    assert Solution.clumsy(10) == 12
