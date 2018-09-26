class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        bits = bin(N)[2:]
        pre, ret = -1, 0

        for i, bit in enumerate(bits):
            if bit == '0':
                continue
            if pre >= 0 and i - pre > ret:
                ret = i - pre
            pre = i
        return ret



if __name__ == '__main__':
    print(Solution().binaryGap(22))
    print(Solution().binaryGap(5))
    print(Solution().binaryGap(6))
    print(Solution().binaryGap(8))







