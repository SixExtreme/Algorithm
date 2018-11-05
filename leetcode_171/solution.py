class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        _sum, n = 0, len(s)
        for i in range(n):
            _sum = _sum * 26 + (ord(s[i]) - 64)
            n -= 1
        return _sum


if __name__ == '__main__':
    print(Solution().titleToNumber('AB'))