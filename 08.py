"""
题目描述:
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

解决思路:
第一种:动态规划
"""

# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        if number <= 2:
            return number
        dp = [1 for _ in range(number)]
        dp[1] = 2
        for i in range(2, number):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]

S = Solution()
number = 4
result = S.jumpFloor(number)
print(result)