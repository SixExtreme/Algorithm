class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i, x in enumerate(nums):
            nums[abs(x) - 1] = -abs(nums[abs(x) - 1])
        return [(i + 1) for i, x in enumerate(nums) if x > 0]


if __name__ == '__main__':
    nums = [4, 5, 3, 2, 2, 6]
    print(Solution().findDisappearedNumbers(nums))