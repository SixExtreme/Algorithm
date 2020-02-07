from typing import List


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x < 0:
        #     return False
        # if 0 <= x < 10:
        #     return True
        # nums: List[int] = []
        # while x:
        #     nums.append(x % 10)
        #     x //= 10
        # i, j = 0, len(nums) - 1
        # while i < j:
        #     if nums[i] != nums[j]:
        #         return False
        #     i, j = i + 1, j - 1
        # return True

        if x < 0:
            return False
        if 0 <= x < 10:
            return True
        if x % 10 == 0:
            return False
        y: int = 0
        while x > y:
            y = y * 10 + x % 10
            x //= 10
        return x == y or x == y // 10


def test_solution():
    assert Solution().isPalindrome(121)
    assert not Solution().isPalindrome(-121)
    assert not Solution().isPalindrome(10)
    assert Solution().isPalindrome(11)
