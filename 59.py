"""
题目描述:
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，
第三行按照从左到右的顺序打印，其他行以此类推。
解决思路：
普通的BFS使用队列实现，这里使用两个栈来存储奇数行和偶数行的节点
"""

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        if not pRoot:
            return []
        result = []
        queue1 = []  # 存放奇数行节点
        queue2 = []  # 存放偶数行节点
        queue1.append(pRoot)
        while queue1 or queue2:
            tmp = []
            while queue1:
                node = queue1.pop()
                tmp.append(node.val)
                if node.left:
                    queue2.append(node.left)
                if node.right:
                    queue2.append(node.right)
            if tmp:
                result.append(tmp)
                tmp = []
            while queue2:
                node = queue2.pop()
                tmp.append(node.val)
                if node.right:
                    queue1.append(node.right)
                if node.left:
                    queue1.append(node.left)
            if tmp:
                result.append(tmp)
        return result
