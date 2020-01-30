"""
题目描述
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
解决思路：
用一个另外的字典来储存对应关系
"""

# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        p1 = pHead
        nodes = []
        dict = {}
        if pHead == None:
            return None
        while p1:
            nodes.append(p1)
            p1 = p1.next
        p1 = pHead
        while p1:
            if p1.random:
                dict[nodes.index(p1)] = nodes.index(p1.random)
            else:
                dict[nodes.index(p1)] = -1
            p1 = p1.next
        new_nodes = [RandomListNode(x.label) for x in nodes]
        for i, node in enumerate(new_nodes):
            if i < len(new_nodes)-1:
                node.next = new_nodes[i+1]
            if dict[i] != -1:
                node.random = new_nodes[dict[i]]
        return new_nodes[0] if new_nodes else None