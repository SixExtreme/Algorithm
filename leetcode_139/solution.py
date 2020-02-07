from typing import List, Set, Deque, Optional


class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:
        # def helper(_s: str, _dict: Set[str], start: int) -> bool:
        #     if start == len(_s):
        #         return True
        #     for end in range(start + 1, len(_s) + 1):
        #         if _s[start:end] in words and helper(_s, _dict, end):
        #             return True
        #     return False
        #
        # return helper(s, set(words), 0)

        # def helper(_s: str, _dict: Set[str], start: int, backtrack: List[Optional[bool]]) -> bool:
        #     if start == len(_s):
        #         return True
        #     if not backtrack[start] is None:
        #         return backtrack[start]
        #     for end in range(start + 1, len(_s) + 1):
        #         if _s[start:end] in _dict and helper(_s, _dict, end, backtrack):
        #             backtrack[start] = True
        #             return True
        #     backtrack[start] = False
        #     return False
        #
        # backtrack: List[Optional[bool]] = [None for _ in s]
        # return helper(s, set(words), 0, backtrack)

        from collections import deque

        _dict: Set[str] = set(words)
        queue: Deque[int] = deque([0])
        visit: List[bool] = [False] * len(s)
        while queue:
            start: int = queue.popleft()
            if not visit[start]:
                for end in range(start + 1, len(s) + 1):
                    if s[start:end] in _dict:
                        queue.append(end)
                        if end == len(s):
                            return True
                visit[start] = True
        return False

        # _dict: Set[str] = set(words)
        # dp: List[bool] = [False for _ in range(len(s) + 1)]
        # dp[0] = True
        # for i in range(1, len(s) + 1):
        #     for j in range(0, i):
        #         if dp[j] and s[j:i] in _dict:
        #             dp[i] = True
        #             break
        # return dp[-1]


def test_solution():
    assert Solution().wordBreak('leetcode', ['leet', 'code'])
    assert Solution().wordBreak('applepenapple', ['apple', 'pen'])
    assert not Solution().wordBreak('catsandog', ['cats', 'dog', 'sand', 'and', 'cat'])


if __name__ == '__main__':
    assert Solution().wordBreak('leetcode', ['leet', 'code'])
