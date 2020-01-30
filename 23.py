"""
题目描述:
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
解决思路:
链接：https://www.nowcoder.com/questionTerminal/a861533d45854474ac791d90e447bafd?f=discussion
来源：牛客网
后序遍历的序列中，最后一个数字是树的根节点 ，数组中前面的数字可以分为两部分：
第一部分是左子树节点的值，都比根节点的值小；第二部分是右子树节点的值，都比根节点的值大，
后面用递归分别判断前后两部分 是否符合以上原则
"""

# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if sequence == None or len(sequence)==0:
            return False
        length = len(sequence)
        root = sequence[-1]
        # 找出左子树
        for i in range(length):
            if sequence[i] > root:
                break
        # 找出右子树
        for j in range(i, length):
            if sequence[j] < root:
                return False
        # 判断左子树是否为BST
        left = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[0:i])
        # 判断右子树是否为BST
        right = True
        if i < length-1:
            right = self.VerifySquenceOfBST(sequence[i:-1])
        return left and right