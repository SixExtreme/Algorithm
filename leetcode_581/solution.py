import copy

class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _nums = copy.copy(nums)
        _nums.sort()
        i, j = 0, len(nums) - 1
        while nums[i] == _nums[i] and i < j:
            i += 1
        while nums[j] == _nums[j] and j > i:
            j -= 1
        return 0 if i == j else j - i + 1