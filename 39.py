"""
题目描述:
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
解决思路：
第一种：在38题计算二叉树深度的基础上，每一次递归都比较左右子树深度差，如果有超过1的，就不是平衡二叉树
第二种：在第一种的基础上，加多了剪枝，减少了对子树的重复遍历。如果子树是平衡二叉树，则返回子树的高度；
如果发现子树不是平衡二叉树，则直接停止遍历，这样至多只对每个结点访问一次。
"""

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 第一种
# class Solution:
#     def __init__(self):
#         self.isBalanced = True
#
#     def IsBalanced_Solution(self, pRoot):
#         if pRoot is None:
#             return self.isBalanced
#         self.TreeDepth(pRoot)
#         return self.isBalanced
#
#
#     def TreeDepth(self, pRoot):
#         if pRoot is None:
#             return 0
#         left_depth = self.TreeDepth(pRoot.left)
#         right_depth = self.TreeDepth(pRoot.right)
#         if abs(left_depth-right_depth) > 1:
#             self.isBalanced = False
#         return left_depth+1 if left_depth > right_depth else right_depth+1

# 第二种
class Solution:
    def IsBalanced_Solution(self, pRoot):
        if pRoot is None:
            return True
        return self.TreeDepth(pRoot) != -1

    def TreeDepth(self, pRoot):
        if pRoot is None:
            return 0
        left_depth = self.TreeDepth(pRoot.left)
        if left_depth == -1:
            return -1
        right_depth = self.TreeDepth(pRoot.right)
        if right_depth == -1:
            return -1
        if abs(left_depth-right_depth) > 1:
            return -1
        else:
            return 1 + max(left_depth, right_depth)

