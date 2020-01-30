"""
题目描述:
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
解决思路:
第一种：先用一个列表，将二叉搜索树中序遍历的结果存储下来，即排序好的列表；再在列表中转换链表指向。
"""

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def getOrderList(self, array, root):
        if not root:
            return []
        if root.left:
            self.getOrderList(array, root.left)
        array.append(root)
        if root.right:
            self.getOrderList(array, root.right)
        return array
    def Convert(self, pRootOfTree):
        array = []
        array = self.getOrderList(array, pRootOfTree)
        for i, node in enumerate(array[:-1]):
            node.right = array[i+1]
            array[i+1].left = node
        return array[0] if len(array)!=0 else None


S = Solution()
node = TreeNode(3)
node.left = TreeNode(2)
node.right = TreeNode(4)
tmp = node.left
tmp.left = TreeNode(1)
tmp = node.right
tmp.right = TreeNode(5)
array = []
array = S.getOrderList(array, node)
print(array)
