"""
题目描述:
输入一个链表，反转链表后，输出新链表的表头。
解决思路：
第一种：遍历后输出到一个数组，新建链表，插入数组栈弹出的值
第二种：用多个指针，分别指向当前结点和前一个结点
"""

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 第一种
# class Solution:
#     # 返回ListNode
#     def ReverseList(self, pHead):
#         array = []
#         head = pHead
#         while head:
#             array.append(head.val)
#             head = head.next
#         if len(array) == 0:
#             return None
#         node = ListNode(array.pop())
#         while len(array) > 0:
#             tmp = ListNode(array.pop())
#             head = node
#             while head.next:
#                 head = head.next
#             head.next = tmp
#         return node

# 第二种
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if pHead==None or pHead.next==None:
            return pHead
        pre = None
        cur = pHead
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

node = ListNode(1)
for i in range(2, 11):
    tmp = ListNode(i)
    head = node
    while head.next:
        head = head.next
    head.next = tmp

S = Solution()
tmp = node
while tmp:
    print(tmp.val)
    tmp = tmp.next
node = S.ReverseList(node)
while node:
    print(node.val)
    node = node.next