"""
题目描述:
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
解决思路:
递归，f(n)=f(n-1)+f(n-2)+...+f(1), f(n-1)=f(n-2)+f(n-3)+...+f(1),易得f(n)=2f(n-1), 递推公式就是2^(n-1)
"""


# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        if number <= 1:
            return number
        return self.Power(2, number-1)

    # 快速幂, a的b次方
    def Power(self, base, exponent):
        # write code here
        flag = 1
        re = 1
        tmp = base
        if exponent == 0:  # 等于0的情况
            return 1
        if exponent < 0:  # 小于0的时候，设置一个flag,用于返回的时候做判断
            flag = 0
            exponent = abs(exponent)

        while exponent > 0:  # 大于0的情况
            if exponent & 1 == 1:
                re = re * tmp  # 如果是奇数，奇数减一就是偶数
            exponent >>= 1  # 右移动一位就是除以2
            tmp = tmp * tmp  # 2^6=(2*2)^3
        return re if flag else 1 / re


S = Solution()
number = 4
result = S.jumpFloorII(number)
print(result)