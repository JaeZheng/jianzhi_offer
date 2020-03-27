"""
题目描述:
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

解决思路:
第一种：编程语言自带的replace函数
第二种：遍历插入
第三种：先从前往后遍历计算空格的数目，再从后往前替换
"""


# -*- coding:utf-8 -*-
# 解法二
# class Solution:
#     # s 源字符串
#     def replaceSpace(self, s):
#         # write code here
#         result = []
#         for ch in s:
#             if ch != " ":
#                 result.append(ch)
#             else:
#                 result.append("%")
#                 result.append("2")
#                 result.append("0")
#         return "".join(result)


# 解法三
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        num_of_space = 0
        # 遍历计算空格数目
        for ch in s:
            if ch == " ":
                num_of_space += 1
        new_length = len(s)+num_of_space*2
        old_length = len(s)
        result = [" " for _ in range(new_length)]
        # 无空格，则直接返回
        if new_length == old_length:
            return s
        # 扩展数组
        for i in range(0, new_length-old_length):
            s += " "
        old_index = old_length - 1
        while old_index >= 0:
            if s[old_index] != " ":
                result[old_index+2*num_of_space] = s[old_index]
                old_index -= 1
            else:
                result[old_index+2*num_of_space] = '0'
                result[old_index-1+2*num_of_space] = '2'
                result[old_index-2+2*num_of_space] = '%'
                old_index -= 1
                num_of_space -= 1
        return ''.join(result)


S = Solution()
s = "We Are Happy"
result = S.replaceSpace(s)
print(result)