class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        mask = ~0
        while mask & num:
            mask <<= 1
            print(bin(mask))
        return ~mask & ~num

if __name__ == '__main__':
    ret = Solution().findComplement(5)
    print(ret)