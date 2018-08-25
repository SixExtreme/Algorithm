class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sa, sb = 0, 0
        for i, x in enumerate(nums):
            if i % 2 == 0:
                sa = max(sa + x, sb)
            else:
                sb = max(sb + x, sa)
        return max(sa, sb)