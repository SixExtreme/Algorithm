from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def flatten(self):
        flat, queue = [], deque([self])
        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    flat.append((node.val, node.left.val))
                if node.right:
                    queue.append(node.right)
                    flat.append((node.val, node.right.val))
        return flat




# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
#         if len(preorder) != len(inorder):
#             return None
#         if len(preorder) == 0 or len(inorder) == 0:
#             return None
        
#         index_inorder = {x: i for i, x in enumerate(inorder)}
#         index_first = index_inorder[preorder[0]]

#         left_inorder = inorder[:index_first]
#         right_inorder = inorder[index_first + 1:]
#         left_preorder = preorder[1:1+len(left_inorder)]
#         right_preorder = preorder[1+len(left_inorder):]

#         root = TreeNode(preorder[0])
#         root.left = self.buildTree(left_preorder, left_inorder)
#         root.right = self.buildTree(right_preorder, right_inorder)
#         return root

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) != len(inorder):
            return None
        if len(preorder) == 0 or len(inorder) == 0:
            return None

        root = TreeNode(preorder[0])
        stack = [root]
        inorder_index = 0
        for i in range(1, len(preorder)):
            node = stack[-1]
            if node.val != inorder[inorder_index]:
                node.left = TreeNode(preorder[i])
                stack.append(node.left)
            else:
                while stack and stack[-1].val == inorder[inorder_index]:
                    node = stack.pop()
                    inorder_index += 1
                node.right = TreeNode(preorder[i])
                stack.append(node.right)
            # print(i, inorder_index, [node.val for node in stack],root.flatten())
        return root


if __name__ == '__main__':
    root = Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])



