"""
题目描述:
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

解决思路:
第一种：暴力法，逐个遍历
第二种：暴力法，逐行二分查找
第三种：从左下或右上开始找。比如左上：如果<target，按行递增，如果>target，按列递减。
弟四种：两次(按行+按列)二分查找。先按行二分查找，找到<=target的值，再按列二分查找。
"""


# -*- coding:utf-8 -*-
class Solution:
    """从左下开始找"""
    # array 二维列表
    def Find(self, target, array):
        # write code here
        rows = len(array)
        if rows == 0:
            return False
        cols = len(array[0])
        if cols == 0:
            return False
        i, j = rows-1, 0
        while i >= 0 and j <= rows-1:
            if array[i][j] > target:
                i -= 1
            elif array[i][j] < target:
                j += 1
            else:
                return True
        return False


# import numpy as np
# class Solution:
#     """二次(按行+按列)二分查找"""
#     # array 二维列表
#     def Find(self, target, array):
#         rows = len(array)
#         if rows == 0:
#             return False
#         cols = len(array[0])
#         if cols == 0:
#             return False
#         array = np.array(array)
#         # 按行
#         result, index = self.binarySearch(array[0,:], 0, len(array[0,:])-1, target)
#         if result: return result
#         else:
#             # 按列
#             result, index = self.binarySearch(array[:,index], 0, len(array[:,index])-1, target)
#             if result: return result
#         # 按列
#         result, index = self.binarySearch(array[:,0], 0, len(array[:,0]) - 1, target)
#         if result: return result
#         else:
#             # 按行
#             result, index = self.binarySearch(array[index,:], 0, len(array[index,:]) - 1, target)
#             if result: return result
#         return False
#
#     def binarySearch(self, array, l, r, target):
#         while l < r:
#             mid = int((l+r)/2)
#             if array[mid] < target:
#                 l = mid
#             elif array[mid] > target:
#                 r = mid-1
#             else:
#                 return True, mid
#         return False, l


S = Solution()
target, array = 7,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
result = S.Find(target, array)
print(result)
