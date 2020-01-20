"""
题目描述:
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
解决思路:
递归,但是代入公式复杂度是2的n次方，会超时。所以改用数组存储或者是两个临时变量存储，时间换空间
"""

# -*- coding:utf-8 -*-
# # 递归公式，会超时
# class Solution:
#     def Fibonacci(self, n):
#         if n == 0:
#             return 0
#         if n == 1 or n == 2:
#             return 1
#         return self.Fibonacci(n-1) + self.Fibonacci(n-2)

# # 数组存储
# class Solution:
#     def Fibonacci(self, n):
#         if n <= 1:
#             return n
#         ans = [0 for _ in range(n+1)]
#         ans[1] = 1
#         for i in range(2,n+1):
#             ans[i] = ans[i-1] + ans[i-2]
#         return ans[n]


# 临时变量存储
class Solution:
    def Fibonacci(self, n):
        if n <= 1:
            return n
        tmp_1 = 0
        tmp_2 = 1
        for i in range(2, n+1):
            result = tmp_1 + tmp_2
            tmp_1 = tmp_2
            tmp_2 = result
        return result


S = Solution()
n = 5
result = S.Fibonacci(n)
print(result)