from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        nfull, queue = 1, deque([root])
        while queue:
            is_break, qsize = False, len(queue)
            for _ in range(qsize):
                node = queue.popleft()
                if node.left and node.right:
                    if is_break:
                        return False
                    queue.append(node.left)
                    queue.append(node.right)
                elif node.left and not node.right:
                    if is_break:
                        return False
                    is_break = True
                    queue.append(node.left)
                elif not node.left and node.right:
                    return False
                else:
                    is_break = True
            if qsize != nfull:
                return len(queue) == 0
            nfull *= 2
        return True


def test_solution():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    assert Solution().isCompleteTree(root)

    root.left.left.left = TreeNode(7)
    assert not Solution().isCompleteTree(root)

    root.left.left.left = None
    root.right.left = None
    root.right.right = TreeNode(7)
    assert not Solution().isCompleteTree(root)
