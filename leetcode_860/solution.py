class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        c5, c10 = 0, 0
        for bill in bills:
            if bill == 5:
                c5 += 1
            if bill == 10:
                c10 += 1
                if c5 >= 1:
                    c5 -= 1
                else:
                    return False
            if bill == 20:
                if c10 >= 1 and c5 >= 1:
                    c5 -= 1
                    c10 -= 1
                elif c5 >= 3:
                    c5 -= 3
                else:
                    return False
        return True
