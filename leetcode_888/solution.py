class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        seta, setb = set(A), set(B)
        suma, sumb = sum(A), sum(B)

        avg = (suma + sumb) // 2
        for x in seta:
            expect = avg - (suma - x)
            if expect in setb:
                return (x, expect)




if __name__ == '__main__':
    print(Solution().fairCandySwap([1, 1], [2, 2]))