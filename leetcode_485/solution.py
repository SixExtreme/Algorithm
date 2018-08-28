class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _max, _count = 0, 0
        for x in nums:
            if x != 1:
                _count = 0
            else:
                _count += 1
            _max = max(_max, _count)
        return _max