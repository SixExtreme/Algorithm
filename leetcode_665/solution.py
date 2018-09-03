class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n, cnt = len(nums), 0
        for i in range(1, n):
            if cnt > 1:
                return False
            if nums[i - 1] > nums[i]:
                cnt += 1
                if i - 2 < 0 or nums[i - 2] <= nums[i]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
        return cnt <= 1


if __name__ == '__main__':
    nums = [4, 2, 1]
    print(Solution().checkPossibility(nums))
