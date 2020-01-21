"""
题目描述:
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
保证base和exponent不同时为0
"""

# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        if base == 0:
            return 0
        if exponent == 0:
            return 1
        return base ** int(exponent)

S = Solution()
base, exponent = 2.0, 3.2
result = S.Power(base, exponent)
print(result)