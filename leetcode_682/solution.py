class Solution:
    def calPoints(self, ops):
        '''
        :type ops: List[str]
        :rtype: int
        '''
        stk = []
        for op in ops:
            if op is 'C':
                stk.pop()
            elif op is 'D':
                stk.append(2 * int(stk[-1]))
            elif op is '+':
                stk.append(stk[-1] + stk[-2])
            else:
                stk.append(int(op))
        return sum(stk)


if __name__ == '__main__':
    ops = ['5','2','C','D','+']
    print(Solution().calPoints(ops))

    ops = ['5','-2','4','C','D','9','+','+']
    print(Solution().calPoints(ops))

