class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count, major = 1, nums[0]
        for i in range(1, len(nums)):
            if count == 0:
                count += 1
                major = nums[i]
            else:
                if nums[i] != major:
                    count -= 1
                else:
                    count += 1
        return major
