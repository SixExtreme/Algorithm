from typing import List


class Solution:
    @staticmethod
    def duplicateZeros(arr: List[int]) -> None:
        # i = 0
        # while i < len(arr):
        #     if arr[i] > 0:
        #         i += 1
        #     else:
        #         for j in range(len(arr) - 1, i, -1):
        #             arr[j] = arr[j - 1]
        #             print(arr)
        #         i += 2
        pass


def test_solution():
    arr = [1, 0, 2, 3, 0, 4, 5, 0]
    Solution.duplicateZeros(arr)
    assert arr == [1, 0, 0, 2, 3, 0, 0, 4]