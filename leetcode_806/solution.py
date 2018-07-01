class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        line, length = 1, 0
        for c in S:
            width = widths[ord(c) - ord('a')]
            if length + width <= 100:
                length += width
            else:
                line, length = line + 1, width
        return [line, length]
                



if __name__ == '__main__':
    widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    S = "abcdefghijklmnopqrstuvwxyz"
    ret = Solution().numberOfLines(widths, S)
    print(ret)