class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        _sum, _max = 0, nums[0]
        for x in nums:
            _sum += x
            _sum = max(_sum, x)
            if _sum > _max:
                _max = _sum
        return _max

