class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # if not nums:
        #     return 0
        # for i in range(len(nums)):
        #     if nums[i] >= target:
        #         return i
        # else:
        #     return len(nums)

        # l, h = 0, len(nums) - 1
        # while l <= h:
        #     m = (l + h) // 2
        #     if nums[m] == target:
        #         return m
        #     elif nums[m] > target:
        #         h = m - 1
        #     else:
        #         l = m + 1
        # return l

        # l, r = 0, len(nums) - 1
        # while l <= r:
        #     m = (l + r) // 2
        #     if nums[m] == target:
        #         return m
        #     elif nums[m] > target:
        #         r = m - 1
        #     else:
        #         l = m + 1
        # return l

        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m
        return l if nums[l] >= target else l + 1



if __name__ == '__main__':
    print(Solution().searchInsert([1, 3, 5, 6], 5))
    print(Solution().searchInsert([1, 3, 5, 6], 2))
    print(Solution().searchInsert([1, 3, 5, 6], 7))
    print(Solution().searchInsert([1, 3, 5, 6], 0))
