"""
题目描述:
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
解决思路:
写一个函数判断A树是否包含B树，再递归调用
"""

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if pRoot1 == None or pRoot2 == None:
            return False
        return self.Tree1HasTree2(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or \
               self.HasSubtree(pRoot1.right, pRoot2)

    def Tree1HasTree2(self, tree1, tree2):
        if tree2 == None:
            return True
        if tree1 == None:
            return False
        if tree1.val != tree2.val:
            return False
        return self.Tree1HasTree2(tree1.left, tree2.left) and self.Tree1HasTree2(tree1.right, tree2.right)
