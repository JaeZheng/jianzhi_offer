"""
题目描述:
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
解决思路:
两个指针对应两个链表，对比当前值，小的值插入并将当前链表指针向后移。注意一个链表为空后剩下另一个链表全插入
"""

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        dummy = ListNode(0)
        p = dummy
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                p.next = pHead1
                pHead1 = pHead1.next
                p = p.next
            else:
                p.next = pHead2
                pHead2 = pHead2.next
                p = p.next
        if pHead1:
            p.next = pHead1
        if pHead2:
            p.next = pHead2
        return dummy.next