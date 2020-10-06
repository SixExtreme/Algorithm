from typing import List


class Solution:
    def searchFirst(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        i, j = 0, len(nums) - 1
        while i < j:
            mid = i + (j - i) // 2
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid
        return i if nums[i] == target else -1

    def searchLast(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        # i, j = 0, len(nums) - 1
        # while i < j:
        #     mid = i + (j - i) // 2
        #     if nums[mid] <= target:
        #         i = mid + 1
        #     else:
        #         j = mid
        # if nums[i] == target:
        #     return i
        # elif nums[i - 1] == target:
        #     return i - 1
        # else:
        #     return -1
        i, j = 0, len(nums) - 1
        while i < j:
            mid = i + (j - i) // 2 + 1
            if nums[mid] <= target:
                i = mid
            else:
                j = mid - 1
        return i if nums[i] == target else -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        if len(nums) == 1:
            return [0, 0] if nums[0] == target else [-1, -1]

        left = self.searchFirst(nums, target)
        if left == -1:
            return [-1, -1]
        return [left, self.searchLast(nums, target)]




if __name__ == '__main__':
    # print(Solution().searchRange([2, 2], 2))
    # print(Solution().searchRange([1, 4], 4))
    # print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
    # print(Solution().searchRange([5, 7, 7, 8, 8, 10], 6))

    # print(Solution.searchFirst([], 9))
    # print(Solution.searchFirst([9, 10], 9))
    # print(Solution.searchFirst([8, 9], 9))
    # print(Solution.searchFirst([9, 9, 10], 9))
    # print(Solution.searchFirst([8, 9, 9], 9))
    # print(Solution.searchFirst([8, 9, 9, 10], 9))
    #
    # print("---")

    print(Solution().searchLast([], 9))
    print(Solution().searchLast([9, 10], 9))
    print(Solution().searchLast([8, 9], 9))
    print(Solution().searchLast([9, 9, 10], 9))
    print(Solution().searchLast([8, 9, 9], 9))
    print(Solution().searchLast([8, 9, 9, 10], 9))


