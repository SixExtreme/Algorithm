# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


from typing import Optional, Deque
from collections import deque


class Solution:
    @staticmethod
    def connect(root: Optional[Node]) -> Optional[Node]:
        if root is None:
            return root
        queue: Deque[Node] = deque([root])
        while queue:
            size: int = len(queue)
            prev: Optional[Node] = None
            for _ in range(size):
                node: Node = queue.popleft()
                if prev is None:
                    prev = node
                else:
                    prev.next = node
                    prev = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root

