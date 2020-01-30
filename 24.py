"""
题目描述
输入一棵二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)
解决思路：
深度优先搜索DFS，直到叶子节点，把经过路径的值加起来与所给整数比较，将符合条件的加进去结果数组中
"""

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        result = []
        self.nums = expectNumber
        if root == None:
            return []
        self.DFS(root, result, [root.val])
        return result

    def DFS(self, root, result, path):
        if root.left == None and root.right == None and sum(path)==self.nums:
            result.append(path)
        if root.left != None:
            self.DFS(root.left, result, path+[root.left.val])
        if root.right != None:
            self.DFS(root.right, result, path + [root.right.val])