"""
题目描述:
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
解决思路：
第一种：放入字典，再检索字典
第二种：先排序，再比较当前值与前后值是否相等，如果都不相等，则只出现一次。注意边界。
"""

# -*- coding:utf-8 -*-
# 第一种
# class Solution:
#     # 返回[a,b] 其中ab是出现一次的两个数字
#     def FindNumsAppearOnce(self, array):
#         number_set = set(array)
#         number_dict = {}
#         for i in number_set:
#             number_dict[i] = 0
#         for i in array:
#             number_dict[i] += 1
#         result = []
#         for k, v in number_dict.items():
#             if v == 1:
#                 result.append(k)
#         return result

# 第二种
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        result = []
        array = sorted(array)
        if array[0] != array[1]:
            result.append(array[0])
        if array[-1] != array[-2]:
            result.append(array[-1])
        if len(result)==2:
            return result
        for i in range(1, len(array)-1):
            if array[i]!=array[i-1] and array[i]!=array[i+1]:
                result.append(array[i])
        return result



array = [1,1,2,3,4,4,5,5]
S = Solution()
result = S.FindNumsAppearOnce(array)
print(result)