from typing import Deque
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sum(self, root: TreeNode) -> int:
        _sum: int = 0
        if not root:
            return _sum
        queue: Deque[TreeNode] = deque([root])
        while queue:
            size: int = len(queue)
            for _ in range(size):
                node: TreeNode = queue.popleft()
                _sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return _sum

    def findTilt(self, root: TreeNode) -> int:
        if not root:
            return 0
        tilt: int = abs(self.sum(root.left) - self.sum(root.right))
        return tilt + self.findTilt(root.left) + self.findTilt(root.right)


def test_solution():
    root: TreeNode = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert Solution().findTilt(root) == 1
