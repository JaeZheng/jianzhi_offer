"""
题目描述
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
"""
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        if not pHead:
            return None
        val_list = []
        p1 = pHead
        while p1:
            val_list.append(p1.val)
            p1 = p1.next
        val_set = [i for i in val_list if val_list.count(i)==1]
        if len(val_set) == 0:
            return None
        dummy = ListNode(0)
        p2 = dummy
        p1 = pHead
        while p1:
            if p1.val in val_set:
                p2.next = ListNode(p1.val)
                p2 = p2.next
            p1 = p1.next
        return dummy.next


dummy = ListNode(1)
p = dummy
p.next = ListNode(2)
p = p.next
p.next = ListNode(3)
p = p.next
p.next = ListNode(3)
p = p.next
p.next = ListNode(4)
p = p.next
p.next = ListNode(4)
p = p.next
p.next = ListNode(5)
p = p.next
p1 = dummy
while p1:
    print(p1.val)
    p1 = p1.next
S = Solution()
p2 = S.deleteDuplication(dummy)
while p2:
    print(p2.val)
    p2 = p2.next

