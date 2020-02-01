from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # m1, m2 = '', ''
        # for ch in letters:
        #     if ch == target:
        #         continue
        #     if ch > target:
        #         m1 = ch if m1 == '' else min(m1, ch)
        #     m2 = ch if m2 == '' else min(m2, ch)
        # return m1 if m1 != '' else m2

        for ch in letters:
            if ch > target:
                return ch
        return letters[0]


def test_solution():
    assert Solution().nextGreatestLetter(['c', 'f', 'j'], 'a') == 'c'
    assert Solution().nextGreatestLetter(['c', 'f', 'j'], 'c') == 'f'
    assert Solution().nextGreatestLetter(['c', 'f', 'j'], 'd') == 'f'
    assert Solution().nextGreatestLetter(['c', 'f', 'j'], 'j') == 'c'
    assert Solution().nextGreatestLetter(['c', 'f', 'j'], 'k') == 'c'
