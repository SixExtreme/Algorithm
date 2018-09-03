from copy import copy

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # n, _nums = len(nums), copy(nums)
        # while k > n:
        #     k -= n
        # for i in range(n):
        #     if i < k:
        #         nums[i] = _nums[n - k + i]
        #     else:
        #         nums[i] = _nums[i - k]

        def reverse(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i, j = i + 1, j - 1

        n = len(nums)
        while k >= n:
            k -= n
        if k == 0:
            return
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)




if __name__ == '__main__':
    # nums = [1]
    # Solution().rotate(nums, 4)
    # print(nums)
    nums = [1, 3, 2, 4, 5, 6, 7]
    i, j = 0, 3
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i, j = i + 1, j - 1
    i, j = 4, 6
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i, j = i + 1, j - 1
    print(nums)
