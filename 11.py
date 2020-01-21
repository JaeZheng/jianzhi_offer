"""
题目描述:
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

解决思路:
第一种：n&(n-1),把一个整数减去1，再和原整数做与运算,会把该整数最右边一个1变成0.
那么一个整数的二进制有多少个1，就可以进行多少次这样的操作。
第二种：转为字符串之后计数
第三种：用1和n的每一位按位与
"""

# -*- coding:utf-8 -*-
# 第一种
# class Solution:
#     def NumberOf1(self, n):
#         # python需要把负数统一转为补码
#         n = n & 0xffffffff
#         count = 0
#         while n:
#             count += 1
#             n = n & (n-1)
#         return count

# 第二种
class Solution:
    def NumberOf1(self, n):
        # python需要把负数统一转为补码
        n = n & 0xffffffff
        n = str(bin(n))
        return n.count("1")


S = Solution()
n = 10
result = S.NumberOf1(n)
print(result)