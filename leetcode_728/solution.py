class Solution:

    def judge(self, num):
        tmp = num
        while tmp:
            k = tmp % 10
            if k != 0 and num % k == 0:
                tmp //= 10
            else:
                return False
        return True


    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        return [x for x in range(left, right + 1) if self.judge(x)]
        