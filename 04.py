"""
题目描述:
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回

解决思路：
先从前序遍历数组找到根节点（数组第一个值），然后找到中序遍历数组中根节点的位置，便能割开左子树和右子树。
对左子树和右子树都进行同样的递归遍历。
"""

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if len(pre) == 0 or len(tin) == 0:
            return None
        # 树的根节点是前序遍历数组的第一个值
        root = TreeNode(pre[0])
        # 找到中序遍历数组中根节点的位置
        root_idx = 0
        for i in tin:
            if i == root.val:
                break
            root_idx += 1
        # 对左子树进行递归遍历
        root.left = self.reConstructBinaryTree(pre[1:1+root_idx], tin[0:root_idx])
        # 对右子树进行递归遍历
        root.right = self.reConstructBinaryTree(pre[root_idx+1:], tin[root_idx+1:])
        return root


pre = [1,2,4,7,3,5,6,8]
tin = [4,7,2,1,5,3,8,6]
S = Solution()
result = S.reConstructBinaryTree(pre, tin)
root = result
while root:
    print(root.val)
    root = root.left
root = result
while root:
    print(root.val)
    root = root.right