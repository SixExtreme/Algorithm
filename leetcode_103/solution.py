from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans, queue = [], deque([root])

        direct = True
        while queue:
            n, lv = len(queue), deque()
            for i in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if direct:
                    lv.append(node.val)
                else:
                    lv.appendleft(node.val)
            ans.append(list(lv))
            direct = not direct
        return ans


def test_solution():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    assert Solution().zigzagLevelOrder(root) == [[3], [20, 9], [15, 7]]
