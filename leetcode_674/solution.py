class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        ret, cnt = 1, 1
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                cnt = 1
            else:
                cnt += 1
            ret = max(ret, cnt)
        return ret

if __name__ == '__main__':
    nums = [1, 2, 5, 8, 0]
    print(Solution().findLengthOfLCIS(nums))