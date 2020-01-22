from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for x in nums:
            # if 10 <= x <= 99:
            #     count += 1
            # elif 1000 <= x <= 9999:
            #     count += 1
            # elif x == 100000:
            #     count += 1
            if 10 <= x <= 99 or 1000 <= x <= 9999 or x == 100000:
                count += 1
        return count


def test_solution():
    assert Solution().findNumbers([12, 345, 2, 6, 7896]) == 2
    assert Solution().findNumbers([555, 901, 482, 1771]) == 1
