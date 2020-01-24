"""
题目描述:
输入一个链表，输出该链表中倒数第k个结点。
解决思路:
第一种：先遍历一次，获取链表长度n，第二次遍历到n-k个结点即可。
"""

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        count = 0
        p1 = head
        while p1:
            p1 = p1.next
            count += 1
        p2 = head
        n = 0
        if k > count:
            return None
        while n < count - k:
            p2 = p2.next
            n += 1
        return p2


node = ListNode(1)
for i in range(2, 11):
    tmp = ListNode(i)
    head = node
    while head.next:
        head = head.next
    head.next = tmp

S = Solution()
k = 2
result = S.FindKthToTail(node, k)
print(result.val)
