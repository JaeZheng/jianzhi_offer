"""
题目描述
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
"""
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        if not pRoot:
            return []
        queue1 = []
        queue2 = []
        result = []
        queue1.append(pRoot)
        while queue1 or queue2:
            tmp = []
            while queue1:
                node = queue1.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue2.append(node.left)
                if node.right:
                    queue2.append(node.right)
            if tmp:
                result.append(tmp)
                tmp = []
            while queue2:
                node = queue2.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue1.append(node.left)
                if node.right:
                    queue1.append(node.right)
            if tmp:
                result.append(tmp)
        return result