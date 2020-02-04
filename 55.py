"""
题目描述:
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
解决思路：
引入辅助数组
"""

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        if not pHead:
            return None
        node_list = []
        p1 = pHead
        while p1:
            if p1 in node_list:
                return p1
            else:
                node_list.append(p1)
                p1 = p1.next
        return None