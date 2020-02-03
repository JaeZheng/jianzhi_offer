"""
题目描述:
统计一个数字在排序数组中出现的次数。
解决思路：
第一种：暴力遍历
第二种：二分查找，查找K出现的第一个索引和最后一个索引
"""

# -*- coding:utf-8 -*-
# 第一种
# class Solution:
#     def GetNumberOfK(self, data, k):
#         if not data:
#             return 0
#         if len(data)==1:
#             if data[0] == k:
#                 return 1
#             else:
#                 return 0
#         cnt = 0
#         for i in data:
#             if i <= k:
#                 if i == k:
#                     cnt += 1
#             else:
#                 break
#         return cnt


# 第二种
class Solution:
    def GetNumberOfK(self, data, k):
        if not data:
            return 0
        if len(data)==1:
            if data[0] == k:
                return 1
            else:
                return 0
        if self.GetFirstK(data,k)==-1 and self.GetLastK(data,k)==-1:
            return 0
        return self.GetLastK(data,k)-self.GetFirstK(data,k)+1

    def GetFirstK(self, data, k):
        low, high = 0, len(data)-1
        while low <= high:
            mid = (low+high) // 2
            if data[mid] > k:
                high = mid - 1
            elif data[mid] < k:
                low = mid + 1
            else:
                # 当到list[0]或不为k的时候跳出函数
                if mid == low or data[mid-1] != k:
                    return mid
                else:
                    high = mid - 1
        return -1

    def GetLastK(self, data, k):
        low, high = 0, len(data) - 1
        while low <= high:
            mid = (low + high) // 2
            if data[mid] > k:
                high = mid - 1
            elif data[mid] < k:
                low = mid + 1
            else:
                # 当到list[-1]或不为k的时候跳出函数
                if mid == high or data[mid + 1] != k:
                    return mid
                else:
                    low = mid + 1
        return -1

data = [1,2,3,3,3,3,3,3,4,5,6,7]
k = 3
S = Solution()
result = S.GetNumberOfK(data, k)
print(result)