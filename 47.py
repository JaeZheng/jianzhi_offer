"""
题目描述:
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
解决思路：
短路求值+递归
"""
# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        return n and n+self.Sum_Solution(n-1)