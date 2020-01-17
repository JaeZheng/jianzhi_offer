"""
题目描述:
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。

解决思路:
第一种：遍历链表，数组存储，然后数组做出栈处理
第二种：递归，递归函数放在数组添加前面
"""


# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 第一种
# class Solution:
#     # 返回从尾部到头部的列表值序列，例如[1,2,3]
#     def printListFromTailToHead(self, listNode):
#         if listNode is None:
#             return []
#         if listNode.next is None:
#             return [listNode.val]
#         tmp = []
#         result = []
#         head = listNode
#         while head:
#             tmp.append(head.val)
#             head = head.next
#         length = len(tmp)
#         for i in range(1, length+1):
#             result.append(tmp[length-i])
#         return result

# 第一种
# class Solution:
#     # 返回从尾部到头部的列表值序列，例如[1,2,3]
#     def printListFromTailToHead(self, listNode):
#         if listNode is None:
#             return []
#         if listNode.next is None:
#             return [listNode.val]
#         result = []
#         head = listNode
#         while head:
#             result.insert(0, head.val)
#             head = head.next
#         return result

# 第二种
class Solution:
    def __init__(self):
        self.result = []
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if listNode is not None:
            self.printListFromTailToHead(listNode.next)
            self.result.append(listNode.val)
        return self.result

node = ListNode(1)
for i in range(2, 4):
    tmp = ListNode(i)
    head = node
    while head.next:
        head = head.next
    head.next = tmp

S = Solution()
result = S.printListFromTailToHead(node)
print(result)
