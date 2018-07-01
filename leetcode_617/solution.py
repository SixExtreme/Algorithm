class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """

        # 递归(一)
        # if not t1 and not t2:
        #     return
        # if not t1 or not t2:
        #     return t1 or t2
        # else:
        #     t1.val += t2.val
        #     t1.left = self.mergeTrees(t1.left, t2.left)
        #     t1.right = self.mergeTrees(t1.right, t2.right)
        # return t1

        # 递归(二)
        # if not (t1 and t2):
        #     return t1 or t2
        # else:
        #     root = TreeNode(t1.val + t2.val)
        #     root.left = self.mergeTrees(t1.left, t2.left)
        #     root.right = self.mergeTrees(t1.right, t2.right)
        #     return root

        # 递归(三)
        # if not t1 and not t2:
        #     return
        # v1 = t1.val if t1 else 0
        # v2 = t2.val if t2 else 0
        # root = TreeNode(v1 + v2)
        # root.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
        # root.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
        # return root

        # 迭代(双栈)
        # if not t1 or not t2:
        #     return t1 or t2
        # s1, s2 = [t1], [t2]
        # while s1:
        #     n1, n2 = s1.pop(), s2.pop()
        #     n1.val += n2.val
        #     if not n1.right and n2.right:
        #         n1.right = n2.right
        #     elif n1.right and n2.right:
        #         s1.append(n1.right)
        #         s2.append(n2.right)
        #     if not n1.left and n2.left:
        #         n1.left = n2.left
        #     elif n1.left and n2.left:
        #         s1.append(n1.left)
        #         s2.append(n2.left)
        # return t1