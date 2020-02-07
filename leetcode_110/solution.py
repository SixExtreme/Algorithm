# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def isBalanced(self, root: TreeNode) -> bool:

        def H(_root: TreeNode) -> int:
            if _root is None:
                return 0
            return 1 + max(H(_root.left), H(_root.right))

        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        delt_h = abs(H(root.left) - H(root.right))
        return delt_h <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)


def test_solution():
    root1: TreeNode = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    assert Solution().isBalanced(root1)

    root2: TreeNode = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.left = TreeNode(3)
    root2.left.right = TreeNode(3)
    root2.left.left.left = TreeNode(4)
    root2.left.left.right = TreeNode(4)
    assert not Solution().isBalanced(root2)

    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.right = TreeNode(2)
    root3.left.left = TreeNode(3)
    root3.right.right = TreeNode(3)
    root3.left.left.left = TreeNode(4)
    root3.right.right.right = TreeNode(4)
    assert not Solution().isBalanced(root3)

