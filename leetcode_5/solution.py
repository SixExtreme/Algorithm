class Solution:
    def longestPalindrome(self, s: str) -> str:
        # def expand(s: str, p: int, q: int) -> str:
        #     while p >= 0 and q < len(s) and s[p] == s[q]:
        #         p, q = p - 1, q + 1
        #     return s[p + 1:q]
        #
        # if len(s) == 0:
        #     return s
        # ans = s[0]
        # for i in range(len(s)):
        #     odd = expand(s, i, i)
        #     eve = expand(s, i, i + 1)
        #     ans = max(ans, odd, eve, key=len)
        # return ans

        def expand(s: str, p: int, q: int) -> int:
            while p >= 0 and q < len(s) and s[p] == s[q]:
                p, q = p - 1, q + 1
            return q - p - 1

        if len(s) == 0:
            return s
        start, close = 0, 0
        for i in range(len(s)):
            exp: int = max(expand(s, i, i), expand(s, i, i + 1))
            if exp > close - start:
                start = i - (exp - 1) // 2
                close = i + exp // 2
        return s[start:close + 1]


def test_solution():
    assert Solution().longestPalindrome("babad") in {"bab", "aba"}
    assert Solution().longestPalindrome("cbbd") == "bb"
