from typing import List
from copy import copy


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        chars_map = [0 for _ in range(26)]
        for ch in chars:
            chars_map[ord(ch) - 97] += 1
        for word in words:
            match, ref = True, copy(chars_map)
            for ch in word:
                if ref[ord(ch) - 97] > 0:
                    ref[ord(ch) - 97] -= 1
                else:
                    match = False
                    break
            if match:
                ans += len(word)
        return ans


def test_solution():
    assert Solution().countCharacters(["cat", "bt", "hat", "tree"], "atach") == 6
    assert Solution().countCharacters(["hello", "world", "leetcode"], "welldonehoneyr") == 10
