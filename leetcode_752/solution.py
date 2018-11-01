class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        # 0b10100010100010101100 = 665772
        # return sum(665772 >> bin(i).count('1') & 1 for i in range(L, R + 1))

        _set = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}
        return sum(1 for x in range(L, R + 1) if bin(x).count('1') in _set)