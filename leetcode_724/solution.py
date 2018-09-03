class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lsum, rsum = 0, sum(nums)
        for i in range(len(nums)):
            if lsum == rsum - nums[i]:
                return i
            else:
                lsum += nums[i]
                rsum -= nums[i]
        return -1


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().pivotIndex(nums))