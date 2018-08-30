class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        map = dict()
        for i, x in enumerate(nums):
            if x not in map:
                map[x] = [1, i, i]
            else:
                map[x][0], map[x][2] = map[x][0] + 1, i

        degree, length = 0, len(nums)
        for x, item in map.items():
            _degree, _length = item[0], item[2] - item[1] + 1
            if _degree > degree:
                degree, length = _degree, _length
            elif _degree == degree:
                length = min(length, _length)

        return length


if __name__ == '__main__':
    print(Solution().findShortestSubArray([1, 2, 2, 3, 1, 4, 2]))