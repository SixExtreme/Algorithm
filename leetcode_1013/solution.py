from typing import List
from copy import copy


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        # n = len(A)
        # s1, s2 = copy(A), copy(A)
        # i, j = 1, n - 2
        # while i < n and j > -1:
        #     s1[i] += s1[i - 1]
        #     s2[j] += s2[j + 1]
        #     i, j = i + 1, j - 1
        #
        # _sum = s2[0]
        # if _sum % 3 != 0:
        #     return False
        # tmp = _sum // 3
        #
        # for p in range(n):
        #     if s1[p] == tmp:
        #         for q in range(n - 1, p, -1):
        #             if s2[q] == s1[p]:
        #                 return True
        # return False

        sum_all = sum(A)
        if sum_all % 3 != 0:
            return False
        div = sum_all // 3

        tmp, cnt = 0, 0
        for x in A:
            tmp += x
            if tmp == div:
                tmp, cnt = 0, cnt + 1
        return cnt == 3


def test_solution():
    assert Solution().canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1])
    assert not Solution().canThreePartsEqualSum([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1])
    assert Solution().canThreePartsEqualSum([3, 3, 6, 5, -2, 2, 5, 1, -9, 4])
