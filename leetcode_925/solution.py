class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(name) > len(typed):
            return False

        i, j, last = 0, 0, ''
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                last = name[i]
                i += 1
                j += 1
            elif typed[j] == last:
                j += 1
            else:
                return False
        return i == len(name)


def test_solution():
    assert not Solution().isLongPressedName('saeed', 'ssaaedd')
    assert Solution().isLongPressedName('leelee', 'lleeelee')
    assert Solution().isLongPressedName('laiden', 'laiden')
