from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # if len(nums) == 0:
        #     return 0
        # dp_min = [0] * len(nums)
        # dp_max = [0] * len(nums)
        # dp_min[0], dp_max[0] = nums[0], nums[0]
        #
        # ans = nums[0]
        # for i in range(1, len(nums)):
        #     dp_max[i] = max(dp_min[i - 1] * nums[i], dp_max[i - 1] * nums[i], nums[i])
        #     dp_min[i] = min(dp_min[i - 1] * nums[i], dp_max[i - 1] * nums[i], nums[i])
        #     ans = max(ans, dp_max[i])
        # return ans

        # if len(nums) == 0:
        #     return 0
        # ans, dp_min, dp_max = nums[0], nums[0], nums[0]
        # for i in range(1, len(nums)):
        #     pv_max = dp_max
        #     dp_max = max(dp_min * nums[i], max(dp_max * nums[i], nums[i]))
        #     dp_min = min(dp_min * nums[i], min(pv_max * nums[i], nums[i]))
        #     ans = max(ans, dp_max)
        # return ans

        if len(nums) == 0:
            return 0
        ans = nums[0]
        tmp = 1
        for i in range(len(nums)):
            tmp *= nums[i]
            ans = max(ans, tmp)
            if tmp == 0:
                tmp = 1
        tmp = 1
        for i in range(len(nums) - 1, -1, -1):
            tmp *= nums[i]
            ans = max(ans, tmp)
            if tmp == 0:
                tmp = 1
        return ans


def test_solution():
    assert Solution().maxProduct([2, 3, -2, 4]) == 6
    assert Solution().maxProduct([-2, 0, -1]) == 0
    assert Solution().maxProduct([-1, -2, -3, 0]) == 6

