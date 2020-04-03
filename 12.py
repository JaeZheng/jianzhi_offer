"""
题目描述:
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
保证base和exponent不同时为0
解题思路：
要考虑多种情况
"""

# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        if base == 0:
            return 0
        if exponent == 0:
            return 1
        # return base ** int(exponent)
        return self.quick_pow(base, exponent)

    def quick_pow(self, base, exp):
        flag = 1
        re = 1
        tmp = base
        if exp < 0:
            flag = 0
            exp = abs(exp)
        while exp > 0:
            if exp & 1 == 1:
                re = re * tmp
            tmp = tmp * tmp
            exp >>= 1
        return re if flag else 1/re

S = Solution()
base, exponent = 2.0, 3.2
result = S.Power(base, exponent)
print(result)