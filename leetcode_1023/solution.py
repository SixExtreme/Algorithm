from typing import List


class Solution:
    @staticmethod
    def match(query: str, pattern: str) -> bool:
        # i, j = 0, 0
        # if query[i].islower() and pattern[i].islower():
        #     query = 'A' + query
        #     pattern = 'A' + pattern
        # while i < len(query):
        #     if not query[i].isupper():
        #         i += 1
        #     else:
        #         if j < len(pattern) and query[i] == pattern[j]:
        #             i, j = i + 1, j + 1
        #         else:
        #             return False
        #         while i < len(query) and j < len(pattern) and query[i].islower() and pattern[j].islower():
        #             if query[i] == pattern[j]:
        #                 i, j = i + 1, j + 1
        #             else:
        #                 i += 1
        # return j == len(pattern)

        # i, j = 0, 0
        # while i < len(query):
        #     if query[i].islower():
        #         if j >= len(pattern):
        #             i += 1
        #         else:
        #             if query[i] != pattern[j]:
        #                 i += 1
        #             else:
        #                 i, j = i + 1, j + 1
        #     else:
        #         if j >= len(pattern):
        #             return False
        #         else:
        #             if query[i] != pattern[j]:
        #                 return False
        #             else:
        #                 i, j = i + 1, j + 1
        # return j >= len(pattern)

        # i, j = 0, 0
        # while i < len(query):
        #     if query[i].islower():
        #         if j >= len(pattern) or query[i] != pattern[j]:
        #             i += 1
        #         elif j < len(pattern) and query[i] == pattern[j]:
        #             i, j = i + 1, j + 1
        #     else:
        #         if j >= len(pattern) or query[i] != pattern[j]:
        #             return False
        #         elif j < len(pattern) and query[i] == pattern[j]:
        #             i, j = i + 1, j + 1
        # return j >= len(pattern)

        i, j = 0, 0
        while i < len(query):
            if j < len(pattern) and query[i] == pattern[j]:
                i, j = i + 1, j + 1
            elif j >= len(pattern) or query[i] != pattern[j]:
                if query[i].islower():
                    i += 1
                else:
                    return False
        return j >= len(pattern)

    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        return [self.match(query, pattern) for query in queries]


def test_solution():
    assert Solution().camelMatch(
        ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"],
        "FB"
    ) == [True, False, True, True, False]

    assert Solution().camelMatch(
        ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"],
        "FoBa"
    ) == [True, False, True, False, False]

    assert Solution().camelMatch(
        ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"],
        "FoBaT"
    ) == [False, True, False, False, False]

    assert Solution().camelMatch(
        ["CompetitiveProgramming", "CounterPick", "ControlPanel"],
        "CooP"
    ) == [False, False, True]

    assert Solution().camelMatch(
        ["aksvbjLiknuTzqon", "ksvjLimflkpnTzqn", "mmkasvjLiknTxzqn", "ksvjLiurknTzzqbn", "ksvsjLctikgnTzqn",
         "knzsvzjLiknTszqn"],
        "ksvjLiknTzqn"
    ) == [True for _ in range(6)]

    assert Solution().camelMatch(
        ["aksvbjLiknuTzqon", "ksvjLimflkpnTzqn", "mmkasvjLiknTxzqn", "ksvjLiurknTzzqbn", "ksvsjLctikgnTzqn",
         "knzsvzjLiknTszqn"],
        "ksvjLiknTzqn"
    ) == [True, True, True, True, True, True]

# if __name__ == '__main__':
#     assert not Solution().match('FooBar', 'FoBaT')
#     assert not Solution().match('FootBall', 'FoBaT')
