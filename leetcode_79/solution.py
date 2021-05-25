from typing import Set, List, Deque
from collections import deque

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def bfs(i: int, j: int, board: List[List[str]], word: str) -> bool:
            m, n = len(board), len(board[0]) 
            p = 0
            visit, queue = {(i, j)}, deque([(i, j)])
            while p < len(word) and len(queue) > 0:
                len_queue = len(queue)
                

            
            return p == len(word)

        if len(word) == 0:
            return True
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
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
