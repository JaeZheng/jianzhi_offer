"""
题目描述:
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
"""

# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        if not pNode:
            return None
        # 有右子树，则找到右子树的最左孩子
        if pNode.right:
            p = pNode.right
            while p.left:
                p = p.left
            return p
        # 无右子树，分情况
        while pNode.next:
            # 是父节点的左子节点，则下一个是父节点
            if pNode == pNode.next.left:
                return pNode.next
            # 是父节点的右子节点，则继续往上一层父节点找
            else:
                pNode = pNode.next
        return None  # 到根节点都没找到的话返回空