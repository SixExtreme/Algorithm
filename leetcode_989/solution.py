from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        if K == 0:
            return A
        i, carry = len(A) - 1, 0
        while i > -1 or K != 0:
            rem = K % 10
            if i <= -1:
                tmp = rem + carry
                if tmp > 9:
                    A = [tmp % 10, *A]
                    carry = 1
                else:
                    A = [tmp, *A]
                    carry = 0
            else:
                tmp = A[i] + rem + carry
                if tmp > 9:
                    A[i] = tmp % 10
                    carry = 1
                else:
                    A[i] = tmp
                    carry = 0
                i -= 1
            K //= 10
        return A if carry == 0 else [carry, *A]


def test_solution():
    assert Solution().addToArrayForm([7], 993) == [1, 0, 0, 0]
    # assert Solution().addToArrayForm([2, 7, 4], 181) == [4, 5, 5]
    # assert Solution().addToArrayForm([2, 1, 5], 806) == [1, 0, 2, 1]
    # assert Solution().addToArrayForm([9, 9, 9, 9, 9, 9, 9, 9, 9, 9], 1) == [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
