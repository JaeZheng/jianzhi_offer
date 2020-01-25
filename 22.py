"""
题目描述
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
解决思路：
实质就是广度优先搜索BFS，借助一个队列来实现
"""

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if not root:
            return []
        queue = []
        result = []
        queue.append(root)
        while len(queue) > 0:
            node = queue.pop(0)
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result
