"""
题目描述:
请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
输出描述:
如果当前字符流没有存在出现一次的字符，返回#字符。
解决思路：
设定一个队列，如果没出现过就入队。返回第一个元素就是队列头。如果出现第二次就从队列中移出。
"""

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.string_list = []
        self.first_queue = []
    # 返回对应char
    def FirstAppearingOnce(self):
        return self.first_queue[0] if self.first_queue else '#'
    def Insert(self, char):
        if char in self.string_list and char in self.first_queue:
            self.first_queue.remove(char)
        elif char not in self.string_list and char not in self.first_queue:
            self.first_queue.append(char)
        self.string_list.append(char)

S = Solution()
S.Insert('g')
print(S.FirstAppearingOnce())
S.Insert('o')
print(S.FirstAppearingOnce())
S.Insert('o')
S.Insert('g')
S.Insert('l')
S.Insert('l')
print(S.FirstAppearingOnce())