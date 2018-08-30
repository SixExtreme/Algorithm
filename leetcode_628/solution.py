class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f3 = [nums[0], nums[1], nums[2]]
        f3.sort()

        max1, max2, max3 = f3
        min1, min2 = f3[0], f3[1]

        for i in range(3, len(nums)):
            if nums[i] <= min1:
                min1, min2 = nums[i], min1
            elif min1 < nums[i] <= min2:
                min2 = nums[i]

            if nums[i] >= max3:
                max1, max2, max3 = max2, max3, nums[i]
            elif max2 <= nums[i] < max3:
                max1, max2 = max2, nums[i]
            elif max1 <= nums[i] < max2:
                max1 = nums[i]

        return max(max1 * max2 * max3, min1 * min2 * max3)


if __name__ == '__main__':
    nums = [1, 2, 3, 2]
    print(Solution().maximumProduct(nums))