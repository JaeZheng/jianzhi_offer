"""
题目描述
HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,他又发话了:
在古老的一维模式识别中,常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。
但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？
例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。给一个数组，返回它的最大连续子序列的和，
你会不会被他忽悠住？(子向量的长度至少是1)
解决思路：
第一种：暴力破解，n平方遍历
第二种：动态规划，dp数组储存当前元素为起点的最优值
"""
# -*- coding:utf-8 -*-
# 第一种
# class Solution:
#     def FindGreatestSumOfSubArray(self, array):
#         if len(array) == 0:
#             return 0
#         if len(array) == 1:
#             return array[0]
#         result = array[0]
#         for j in range(0, len(array)):
#             tmp = array[j]
#             if tmp >= result:
#                 result = tmp
#             for i in range(j+1, len(array)):
#                 tmp += array[i]
#                 if tmp >= result:
#                     result = tmp
#         return result

# 第二种
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if len(array) == 0:
            return 0
        if len(array) == 1:
            return array[0]
        dp = [0 for _ in array]
        dp[0] = array[0]
        max_sum = array[0]
        for i in range(1, len(array)):
            new_max = dp[i-1] + array[i]
            if new_max > array[i]:
                dp[i] = new_max
            else:
                dp[i] = array[i]
            if dp[i] > max_sum:
                max_sum = dp[i]
        return max_sum


S = Solution()
array = [1,-2,3,10,-4,7,2,-5]
result = S.FindGreatestSumOfSubArray(array)
print(result)