class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [[] for i in range(numRows)]
        rownum, direct = 0, 1
        for ch in s:
            rows[rownum].append(ch)
            rownum += direct
            if rownum == numRows or rownum == -1:
                direct = -direct
                rownum += (2 * direct)
        return ''.join([''.join(row) for row in rows])


def test_solution():
    assert Solution().convert('ABC', 1) == 'ABC'
    assert Solution().convert('LEETCODEISHIRING', 3) == 'LCIRETOESIIGEDHN'
    assert Solution().convert('LEETCODEISHIRING', 4) == 'LDREOEIIECIHNTSG'

