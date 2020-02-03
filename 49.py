"""
题目描述:
将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0
输入描述:
输入一个字符串,包括数字字母符号,可以为空
输出描述:
如果是合法的数值表达则返回该数字，否则返回0
"""

# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        num_list = [str(i) for i in range(10)] + ['+', '-']
        if s == "":
            return 0
        sum = 0
        label = 1
        if s[0] not in num_list:
            return 0
        if s[0] == "+":
            label = 1
        elif s[0] == "-":
            label = -1
        else:
            sum = num_list.index(s[0])
        for ch in s[1:]:
            if ch in num_list:
                sum = sum*10 + num_list.index(ch)
            else:
                sum = 0
                break
        result = sum * label
        return result if -2**31<=result<=2**31-1 else 0

s = "2147483649"
a = 2147483649
print(a)
a = 2 ** 31
print(a)
S = Solution()
result = S.StrToInt(s)
print(result)