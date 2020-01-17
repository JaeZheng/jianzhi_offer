"""
题目描述:
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

解决思路:
第一种：编程语言自带的replace函数
第二种：遍历插入
第三种：先从前往后遍历计算空格的数目，再从后往前替换
"""


# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        result = []
        for ch in s:
            if ch != " ":
                result.append(ch)
            else:
                result.append("%")
                result.append("2")
                result.append("0")
        return "".join(result)


S = Solution()
s = "We Are Happy"
result = S.replaceSpace(s)
print(result)