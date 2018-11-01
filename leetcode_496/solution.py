class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        map, stk = dict(), list()
        for num in nums:
            while stk and stk[-1] < num:
                map[stk.pop()] = num
            stk.append(num)
        for i in range(len(findNums)):
            findNums[i] = map.get(findNums[i], -1)
        return findNums