class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        s = set()
        for i, x in enumerate(nums):
            if i > k:
                s.remove(nums[i - k - 1])
            if x not in s:
                s.add(x)
            else:
                return True
        return False



if __name__ == '__main__':
    nums = [99, 99]
    print(Solution().containsNearbyDuplicate(nums, 2))
