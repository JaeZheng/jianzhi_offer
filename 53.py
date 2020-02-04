"""
题目描述:
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
"""


# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        if len(s) <= 0:
            return False
        has_point, has_e, has_sign = False, False, False
        for i in range(len(s)):
            # 对于符号位的情况
            if s[i] == '+' or s[i] == '-':
                # 如果已经出现过符号位，那么现在这个新的符号位只能在e后面
                if has_sign:
                    if s[i - 1] != 'e' and s[i - 1] != 'E':
                        return False
                else:
                    # 没出现过的话，标志打为True.但是也要保证不是在第一个位置的话，得在e后面
                    has_sign = True
                    if i > 0 and s[i-1] != 'e' and s[i - 1] != 'E':
                        return False
            # 对于e的情况
            elif s[i] == 'e' or s[i] == 'E':
                # 不能有两个e
                if has_e:
                    return False
                else:
                    has_e = True
                    # 但是e不能出现在最后，后面必须跟数字
                    if i == len(s) - 1:
                        return False
            # 对于小数点情况
            elif s[i] == '.':
                # 不能有两个小数点。而且如果已经出现过e了，那么就不能再出现小数点，因为e后面只能是整数
                if has_point or has_e:
                    return False
                else:
                    has_point = True
            # 对于数字情况
            else:
                if s[i] < '0' or s[i] > '9':
                    return False
        return True

s = "-1E-16"
S = Solution()
result = S.isNumeric(s)
print(result)