class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if not nums:
            return nums

        m, n = len(nums), len(nums[0])
        if r * c != m * n:
            return nums

        ret = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(m * n):
            ret[i // c][i % c] = nums[i // n][i % n]
        return ret

if __name__ == '__main__':
    nums = [[1, 2], [3, 4]]
    print(Solution().matrixReshape(nums, 1, 4))