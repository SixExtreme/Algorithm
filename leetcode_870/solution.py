from typing import List
from itertools import permutations


class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        ans, sup = A, 0
        for perm in permutations(A):
            _sup = sum([(1 if perm[i] > B[i] else 0) for i in range(len(B))])
            if _sup > sup:
                ans, sup = list(perm), _sup
        return ans


def test_solution():
    assert Solution().advantageCount([2, 7, 11, 15], [1, 10, 4, 11]) == [2, 11, 7, 15]
    assert Solution().advantageCount([12, 24, 8, 32], [13, 25, 32, 11]) == [24, 32, 8, 12]
