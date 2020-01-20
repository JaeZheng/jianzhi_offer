"""
题目描述:
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
解决思路:
递归，f(n)=f(n-1)+f(n-2)+...+f(1), f(n-1)=f(n-2)+f(n-3)+...+f(1),易得f(n)=2f(n-1)
"""

# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        if number <= 1:
            return number
        return 2 ** (number-1)

S = Solution()
number = 3
result = S.jumpFloorII(number)
print(result)