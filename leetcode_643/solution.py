class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        _sum = sum(nums[:k])
        _max_avg = _sum / k

        for i in range(k, len(nums)):
            _sum -= nums[i - k]
            _sum += nums[i]

            _avg = _sum / k
            if _max_avg < _avg:
                _max_avg = _avg

        return _max_avg


if __name__ == '__main__':
    nums = [1, 12, -5, -6, 50, 3]
    print(Solution().findMaxAverage(nums, 4))

