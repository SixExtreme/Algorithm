from typing import List


class Solution:

    # @staticmethod
    # def compress(chars: List[str]) -> int:
    #     i = 0
    #     while i < len(chars):
    #         cnt, j = 1, i + 1
    #         while j < len(chars) and chars[i] == chars[j]:
    #             cnt += 1
    #             del chars[j]
    #         if cnt == 1:
    #             i += 1
    #         else:
    #             digits = str(cnt)
    #             for ch in reversed(digits):
    #                 chars.insert(i + 1, ch)
    #             i += len(digits) + 1
    #     return len(chars)

    @staticmethod
    def compress(chars: List[str]) -> int:
        index = write = 0
        for i in range(len(chars)):
            if i + 1 == len(chars) or chars[i] != chars[i + 1]:
                chars[write] = chars[index]
                write += 1
                if i > index:
                    for digit in str(i - index + 1):
                        chars[write] = digit
                        write += 1
                index = i + 1
        return write


def test_solution():
    chars = ['a', 'a', 'b', 'b', 'c', 'c', 'c']
    assert Solution().compress(chars) == 6
    print(chars)

    chars = ['a']
    assert Solution().compress(chars) == 1
    print(chars)

    chars = ['a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']
    assert Solution().compress(chars) == 4
    print(chars)
