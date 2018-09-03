class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        snum, sret = set(), set()
        for x in nums:
            if x - k in snum:
                sret.add(x)
            if x + k in snum:
                sret.add(x + k)
            snum.add(x)
        return len(sret)


if __name__ == '__main__':
    nums = [1, 3, 1, 5, 4]
    print(Solution().findPairs(nums, 0))