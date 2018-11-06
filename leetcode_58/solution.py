class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # s, _len = s.strip(), 0
        # for i in range(len(s) - 1, -1, -1):
        #     if s[i] == ' ':
        #         break
        #     _len += 1
        # return _len
        return len(s.strip().split(' ').pop())