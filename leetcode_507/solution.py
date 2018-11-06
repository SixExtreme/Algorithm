class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return False
        _num = 1
        for k in range(2, num // 2 + 1):
            if k * k > num:
                break
            if num % k == 0:
                _num += k + num // k
        return _num == num


if __name__ == '__main__':
    print(Solution().checkPerfectNumber(28))
