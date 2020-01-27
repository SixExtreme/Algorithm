import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        nums = [-num for num in stones]
        heapq.heapify(nums)
        while len(nums) > 1:
            y = heapq.heappop(nums)
            x = heapq.heappop(nums)
            delta = y - x
            if delta != 0:
                heapq.heappush(nums, delta)
        return 0 if len(nums) == 0 else -nums[0]


def test_solution():
    assert Solution().lastStoneWeight([1, 2, 3, 4]) == 0