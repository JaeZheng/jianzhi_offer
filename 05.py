"""
题目描述：
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

解决思路:
一个栈做入队列操作，插入时直接入，另一个栈做出队列操作，入栈由第一个栈弹出，出栈就是出队列
"""

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []
    def push(self, node):
        self.stack_1.append(node)
    def pop(self):
        if len(self.stack_2) <= 0:
            for i in range(len(self.stack_1)):
                self.stack_2.append(self.stack_1.pop())
        if self.stack_2:
            return self.stack_2.pop()
        else:
            return -1

S = Solution()
for i in range(3):
    S.push(i)
print(S.pop())
S.push(4)
print(S.pop())
print(S.pop())
print(S.pop())