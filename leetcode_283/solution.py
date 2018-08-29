class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        bound, i = -1, 0
        while i < len(nums) and bound < len(nums):
            if nums[i] != 0:
                nums[bound + 1], nums[i] = nums[i], nums[bound + 1]
                bound += 1
            i += 1


if __name__ == '__main__':
    nums = [1, 2]
    Solution().moveZeroes(nums)
    print(nums)
