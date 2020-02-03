"""
题目描述:
输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
解决思路：
第一种：递归。即求孩子节点的最大深度，要么是左孩子，要么是右孩子，那么我们只需要对传入的孩子节点递归调用即可。
第二种：BFS。层次遍历，每经过一层就深度加一。
"""

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 第一种
# class Solution:
#     def TreeDepth(self, pRoot):
#         if pRoot is None:
#             return 0
#         left_depth = self.TreeDepth(pRoot.left)
#         right_depth = self.TreeDepth(pRoot.right)
#         return left_depth+1 if left_depth > right_depth else right_depth+1

# 第二种
class Solution:
    def TreeDepth(self, pRoot):
        if pRoot is None:
            return 0
        queue = []
        queue.append(pRoot)
        depth = 0
        while len(queue) != 0:
            size = len(queue)
            depth += 1
            for i in range(size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth
