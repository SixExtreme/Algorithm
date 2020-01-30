# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # if p is None or q is None:
        #     return p is q
        # if p.val != q.val:
        #     return False
        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        def check(n1: TreeNode, n2: TreeNode):
            if n1 is None or n2 is None:
                return n1 is n2
            return n1.val == n2.val

        from collections import deque

        queue = deque([(p, q)])
        while queue:
            p, q = queue.popleft()
            if not check(p, q):
                return False
            if p:
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))
        return True



def test_solution():
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)

    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)

    assert Solution().isSameTree(p, q)

    p.right = None
    q.left = None
    q.right = TreeNode(2)
    assert not Solution().isSameTree(p, q)

    p.right = TreeNode(3)
    q.left = TreeNode(3)
    assert not Solution().isSameTree(p, q)