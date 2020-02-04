"""
题目描述
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
"""

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        if not pRoot:
            return True
        # 比较左右子树是否相同
        return self.common(pRoot.left, pRoot.right)

    def common(self, left, right):
        # 左子树为空，则右子树同为空才能为True
        if not left:
            return not right
        # 左子树不为空，则右子树为空就为False
        if not right:
            return False
        # 左右子树都不为空，根节点值不同则为true
        if left.val != right.val:
            return False
        # 左右子树根节点相同的话，则继续往下比较左的右子树与右的左子树，以及右的右子树和左的左子树
        return self.common(left.left, right.right) and self.common(left.right, right.left)