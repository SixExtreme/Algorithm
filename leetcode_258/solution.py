class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # while num > 9:
        #     acc, _num = 0, num
        #     while _num > 0:
        #         acc += _num % 10
        #         _num //= 10
        #     num = acc
        # return num
        if num < 10:
            return num
        return num % 9 or num // 9


if __name__ == '__main__':
    num = 38
    print(Solution().addDigits(num))


