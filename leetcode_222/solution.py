from typing import Deque
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        ans = 0
        if not root:
            return ans
        queue: Deque[TreeNode] = deque([root])
        while queue:
            size: int = len(queue)
            for _ in range(size):
                node: TreeNode = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                ans += 1
        return ans


def test_solution():
    root: TreeNode = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    assert Solution().countNodes(root) == 6
