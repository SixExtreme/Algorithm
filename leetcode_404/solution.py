from typing import Deque
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
        ans: int = 0
        queue: Deque[TreeNode] = deque([root])
        while queue:
            size: int = len(queue)
            for _ in range(size):
                node: TreeNode = queue.popleft()
                if node.left:
                    if node.left.left is None and node.left.right is None:
                        ans += node.left.val
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans


def test_solution():
    root: TreeNode = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert Solution().sumOfLeftLeaves(root) == 24
