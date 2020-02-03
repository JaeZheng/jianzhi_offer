"""
题目描述:
输入两个链表，找出它们的第一个公共结点。
解决思路:
第一种: 把两个链表的结点都入栈，然后同时出栈（即从后向前遍历），出现相同时加入结果数组，结果数组出栈第一个元素即为第一个公共结点。
第二种：两个链表不知谁长谁短，但是相加起来，到最后的公共结点部分长度是相同的，所以遍历时出现null就跳到另一个链表。
"""

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 第一种
# class Solution:
#     def FindFirstCommonNode(self, pHead1, pHead2):
#         if not pHead1 or not pHead2:
#             return None
#         p1, p2 = pHead1, pHead2
#         l1, l2, result = [], [], []
#         while p1:
#             l1.append(p1)
#             p1 = p1.next
#         while p2:
#             l2.append(p2)
#             p2 = p2.next
#         while l1 and l2:
#             node1 = l1.pop()
#             node2 = l2.pop()
#             if node1 == node2:
#                 result.append(node1)
#         if result:
#             node = result.pop()
#             return node

# 第二种
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if not pHead1 or not pHead2:
            return None
        p1, p2 = pHead1, pHead2
        while p1 != p2:
            p1 = p1.next if p1 else pHead2
            p2 = p2.next if p2 else pHead1
        return p1


a = []
print(a)