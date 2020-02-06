"""
题目描述
给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1），每段绳子的长度记为k[0],k[1],...,k[m]。
请问k[0]xk[1]x...xk[m]可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
输入描述:
输入一个数n，意义见题面。（2 <= n <= 60）
输出描述:
输出答案。
解决思路：
第一种：动态规划。最小子问题：n=2时，分段乘积最大为1.n=3时，分段乘积最大为2.从遍历到n/2即可，因为后面反过来也是一样。
"""

# -*- coding:utf-8 -*-
class Solution:
    def cutRope(self, number):
        if number == 2:
            return 1
        if number == 3:
            return 2
        dp = [0,1,2,3]
        for i in range(4, number+1):
            result = 0
            for j in range(1, i//2+1):
                result = max(result, dp[j]*dp[i-j])
            dp.append(result)
        return dp[number]


number = 8
S = Solution()
result = S.cutRope(number)
print(result)