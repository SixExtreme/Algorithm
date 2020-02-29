from typing import List, Tuple, AnyStr, Optional


class TreeNode:
    def __init__(self, x: int):
        self.val: int = x
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


class Solution:
    # def binaryTreePaths(self, root: TreeNode) -> List[str]:
    #
    #     def helper(node: TreeNode, path: str, paths: List[str]):
    #         if node is None:
    #             return
    #         path += str(node.val)
    #         if node.left is None and node.right is None:
    #             paths.append(path)
    #         else:
    #             path += "->"
    #             helper(node.left, path, paths)
    #             helper(node.right, path, paths)
    #
    #     ans: List[str] = []
    #     helper(root, "", ans)
    #     return ans

    def binaryTreePaths(self, root: TreeNode) -> List[AnyStr]:
        from collections import deque

        ans: List[AnyStr] = []
        if root is None:
            return ans

        stack: List[Tuple[TreeNode, AnyStr]] = [(root, str(root.val))]
        while stack:
            node, path = stack.pop()
            if node.left is None and node.right is None:
                ans.append(path)
            if node.left:
                stack.append((node.left, f"{path}->{node.left.val}"))
            if node.right:
                stack.append((node.right, f"{path}->{node.right.val}"))
        return ans


def test_solution():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    print(Solution().binaryTreePaths(root))


if __name__ == '__main__':

    def test(s: str) -> str:
        s += "."
        return s
    s = "sss"
    print(s, test(s))