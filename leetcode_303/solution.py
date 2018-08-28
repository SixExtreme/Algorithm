# class NumArray:
#
#     def __init__(self, nums):
#         """
#         :type nums: List[int]
#         """
#         n = len(nums)
#         self.sums = [0] * (n + 1)
#         for i in range(1, n + 1):
#             self.sums[i] = nums[i - 1] + self.sums[i - 1]
#
#     def sumRange(self, i, j):
#         """
#         :type i: int
#         :type j: int
#         :rtype: int
#         """
#         return self.sums[j + 1] - self.sums[i]

class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        n = len(nums)
        self.sums = [0] * n
        sum = 0
        for i, x in enumerate(nums):
            sum += x
            self.sums[i] = sum

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.sums[j]
        else:
            return self.sums[j] - self.sums[i - 1]


if __name__ == '__main__':
    nums = [-2, 0, 3, -5, 2, -1]
    arr = NumArray(nums)
    print(arr.sumRange(0, 2))
    print(arr.sumRange(2, 5))
    print(arr.sumRange(0, 5))