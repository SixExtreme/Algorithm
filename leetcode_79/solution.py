from typing import Set, List, Deque
from collections import deque

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directs = [[1, 1], [1, -1], [-1, -1], [-1, 1]]

        def bfs(x: int, y: int) -> bool:
            pos: int = 1
            visit = {(x, y)}
            m: int = len(board)
            n: int = len(board[0])

            while pos < len(word):
                has_next = False
                for (dx, dy) in directs:
                    p, q = x + dx, y + dy
                    if 0 <= p < m and 0 <= q < n and board[p][q] == word[pos]:
                        pos, x, y = pos + 1, p, q
                        visit.add((p, q))
                        break
                if not has_next:
                    break

            return pos == len(word)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != word[0]:
                    continue
                if bfs(i, j, board, word):
                    return True
        return False


def test_solution():
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    assert Solution().exist('ABCCED')
    assert Solution().exist('SEE')
    assert Solution().exist('ABCB')
