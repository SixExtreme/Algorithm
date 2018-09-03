class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        m1, m2, mi = -1, -1, -1
        for i, x in enumerate(nums):
            if x > m2:
                mi = i
                m1, m2 = m2, x
            elif x > m1:
                m1 = x
        if m2 < 2 * m1:
            return -1
        else:
            return mi


if __name__ == '__main__':
    nums = [0, 0, 0, 1]
    print(Solution().dominantIndex(nums))