class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = [0] * 52
        for ch in s:
            if ch.islower():
                counter[ord(ch) - 97] += 1
            else:
                counter[26 + ord(ch) - 65] += 1
        dbl, sig = 0, 0
        for cnt in counter:
            dbl += cnt // 2
            sig += cnt % 2
        return dbl * 2 + (1 if sig > 0 else 0)


def test_solution():
    assert Solution().longestPalindrome('abccccdd') == 7
