class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                del nums[i]
            i += 1
        return len(nums)

        # if len(nums) < 2:
        #     return len(nums)
        # k = 1
        # for i in range(1, len(nums)):
        #     if nums[i] != nums[i - 1]:
        #         nums[k] = nums[i]
        #         k += 1
        # return k


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(Solution().removeDuplicates(nums))