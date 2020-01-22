from string import ascii_lowercase


class Solution:
    @staticmethod
    def freqAlphabets(s: str) -> str:
        stack = []
        for ch in s:
            if ch != '#':
                stack.append(ord(ch) - 48)
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(a * 10 + b)
        return ''.join([ascii_lowercase[i - 1] for i in stack])


def test_solution():
    assert Solution.freqAlphabets('10#11#12') == 'jkab'
    assert Solution.freqAlphabets('1326#') == 'acz'
    assert Solution.freqAlphabets('25#') == 'y'

