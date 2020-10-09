from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        if n == 1:
            return 0 if nums[0] == target else -1
        i, j = 0, len(nums) - 1
        while i < j:
            mid = i + (j - i) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    j = mid
                else:
                    i = mid + 1
            else:
                if nums[mid] < target <= nums[n - 1]:
                    i = mid + 1
                else:
                    j = mid
        return i if nums[i] == target else -1


if __name__ == '__main__':
    print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))
    print(Solution().search([4, 5, 6, 7, 0, 1, 2], 1))
    print(Solution().search([4, 5, 6, 7, 0, 1, 2], 2))
    print(Solution().search([4, 5, 6, 7, 0, 1, 2], 3))
    print(Solution().search([4, 5, 6, 7, 0, 1, 2], 4))
    print(Solution().search([4, 5, 6, 7, 0, 1, 2], 5))
    print(Solution().search([4, 5, 6, 7, 0, 1, 2], 6))
    print(Solution().search([4, 5, 6, 7, 0, 1, 2], 7))

