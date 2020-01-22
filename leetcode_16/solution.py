from typing import List
from itertools import combinations


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # delta = None
        # idxes = [i for i in range(len(nums))]
        # for com in combinations(idxes, 3):
        #     i, j, k = com
        #     _delta = target - (nums[i] + nums[j] + nums[k])
        #     if delta is None:
        #         delta = _delta
        #     if abs(delta) > abs(_delta):
        #         delta = _delta
        # return target - delta
        nums.sort()
        ans = nums[0] + nums[1] + nums[-1]
        for i in range(len(nums) - 2):
            p, q = i + 1, len(nums) - 1
            while p < q:
                _sum = nums[i] + nums[p] + nums[q]
                if abs(target - _sum) < abs(target - ans):
                    ans = _sum
                if _sum > target:
                    q -= 1
                else:
                    p += 1
        return ans


def test_solution():
    assert Solution().threeSumClosest([-1, 2, 1, -4], 1) == 2
