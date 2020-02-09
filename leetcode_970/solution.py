from typing import List


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        xs = [1]
        while xs[-1] <= bound:
            xs.append(xs[-1] * x)
            if xs[-1] <= xs[-2]:
                break
        xs.pop()

        ys = [1]
        while ys[-1] <= bound:
            ys.append(ys[-1] * y)
            if ys[-1] <= ys[-2]:
                break
        ys.pop()

        bucket = [0 for _ in range(bound + 1)]
        for _x in xs:
            for _y in ys:
                tmp = _x + _y
                if tmp > bound:
                    break
                else:
                    bucket[tmp] = 1

        return [i for i, x in enumerate(bucket) if x != 0]


def test_solution():
    assert Solution().powerfulIntegers(2, 3, 10) == [2, 3, 4, 5, 7, 9, 10]
    assert Solution().powerfulIntegers(3, 5, 15) == [2, 4, 6, 8, 10, 14]