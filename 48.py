"""
题目描述:
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
解决思路：
位运算。
两个数异或：相当于每一位相加，而不考虑进位；
两个数相与，并左移一位：相当于求得进位；
重复上述两步，直到进位值为0
"""

# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        while num2 != 0:
            tmp = num1 ^ num2
            num2 = (num1 & num2) << 1
            num1 = tmp & 0xFFFFFFFF
        # python整型无限大，需要检查正负数
        return num1 if num1 >> 31 == 0 else num1 - 4294967296


class Solution:
    def Add(self, num1, num2):
        while num2:
            num1, num2 = (num1^num2)&0xFFFFFFFF, ((num1&num2)<<1)&0xFFFFFFFF
        return num1 if num1 <= 0x7FFFFFFF else ~(num1^0xFFFFFFFF)