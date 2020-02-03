"""
题目描述:
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
输出描述:
对应每个测试案例，输出两个数，小的先输出。
解决思路：
第一种：穷举
第二种：左右夹逼。数学可证排序数组外层的两个数乘积更小。
"""

# -*- coding:utf-8 -*-
# 第一种
# class Solution:
#     def FindNumbersWithSum(self, array, tsum):
#         if len(array) <= 1:
#             return []
#         if len(array) == 2:
#             if array[0]+array[1]==tsum:
#                 return array
#             else:
#                 return []
#         result = []
#         for i in range(len(array)-1):
#             num1 = array[i]
#             for j in range(1, len(array)):
#                 num2 = array[j]
#                 sum = num1 + num2
#                 if sum < tsum:
#                     continue
#                 elif sum > tsum:
#                     break
#                 else:
#                     result.append([num1, num2])
#         if len(result) == 0:
#             return result
#         if len(result) == 1:
#             return result[0]
#         tmp_result = result[0]
#         for i in range(1, len(result)):
#             tmp = result[i][0] * result[i][1]
#             if tmp < tmp_result[0] * tmp_result[1]:
#                 tmp_result = result[i]
#         return tmp_result

# 第二种
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        result = []
        left = 0
        right = len(array)-1
        if left >= right:
            return result
        while left < right:
            sum = array[left] + array[right]
            if sum == tsum:
                result.append(array[left])
                result.append(array[right])
                return result
            elif sum > tsum:
                right -= 1
            else:
                left += 1
        return result
