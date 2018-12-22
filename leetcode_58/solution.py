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

        # return len(s.strip().split(' ').pop())

        j = len(s) - 1
        while j > -1 and s[j] == ' ':
            j -= 1

        l = 0
        while j > -1 and s[j] != ' ':
            l += 1
            j -= 1

        return l