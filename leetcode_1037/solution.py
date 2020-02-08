from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        dx = points[1][0] - points[0][0]
        dy = points[1][1] - points[0][1]
        ex = points[2][0] - points[0][0]
        ey = points[2][1] - points[0][1]
        return dx * ey != ex * dy


def test_solution():
    assert Solution().isBoomerang([[1, 1], [2, 3], [3, 2]])
    assert not Solution().isBoomerang([[1, 1], [2, 2], [3, 3]])