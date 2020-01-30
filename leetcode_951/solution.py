from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        # if root1 is None or root2 is None:
        #     return root1 is root2
        # if root1.val != root2.val:
        #     return False
        # is_rev = self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
        # is_org = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
        # return is_rev or is_org

        from typing import List

        def DFS(root: TreeNode, vals: List[int]):
            if root is None:
                return
            vals.append(root.val)

            lv, rv = -1, -1
            if root.left:
                lv = root.left.val
            if root.right:
                rv = root.right.val

            if lv < rv:
                DFS(root.left, vals)
                DFS(root.right, vals)
            else:
                DFS(root.right, vals)
                DFS(root.left, vals)

        v1, v2 = [], []
        DFS(root1, v1)
        DFS(root2, v2)
        print(v1, v2)
        return v1 == v2



def test_solution():
    root1: TreeNode = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.right.left = TreeNode(6)
    root1.left.right.left = TreeNode(7)
    root1.left.right.right = TreeNode(8)
    
    root2: TreeNode = TreeNode(1)
    root2.left = TreeNode(3)
    root2.right = TreeNode(2)
    root2.left.right = TreeNode(6)
    root2.right.left = TreeNode(4)
    root2.right.right = TreeNode(5)
    root2.right.right.left = TreeNode(8)
    root2.right.right.right = TreeNode(7)

    assert Solution().flipEquiv(root1, root2)
