"""
题目描述
给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。
"""

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        list = self.inorderTravel(pRoot)
        if len(list)==0 or k==0:
            return None
        if len(list) < k:
            return None
        return TreeNode(list[k-1])

    def inorderTravel(self, root):
        if not root:
            return []
        return self.inorderTravel(root.left) + [root.val] + self.inorderTravel(root.right)