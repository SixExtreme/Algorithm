class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        sum, _max = 0, nums[0]
        for x in nums:
            sum += x
            sum = max(sum, x)
            if sum > _max:
                _max = sum
        return _max

